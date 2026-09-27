import os
import threading
import requests
import base64
from datetime import datetime
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env local, se existir
load_dotenv()

# ==============================================================================
# CONFIGURAÇÃO DE PÁGINA DO STREAMLIT & MODO ESCURO INSTITUCIONAL
# ==============================================================================
st.set_page_config(
    page_title="TRILHANDO O CAMINHO DO CÓDIGO",
    page_icon="🤖",
    layout="wide"
)

# Helper para converter imagens locais para base64 (garante exibição perfeita)
def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

cefet_b64 = get_base64_image("assets/logo-cefet.jpg") or get_base64_image("../arquivos-trilhando/Imagens/logo-cefet.jpg")
fapemig_b64 = get_base64_image("assets/logo-fapemig.jpg") or get_base64_image("../arquivos-trilhando/Imagens/logo-fapemig.jpg")

# Inject CSS para réplica 100% idêntica da imagem de exemplo
st.markdown(f"""
<style>
    /* Estilização Geral do Fundo */
    .stApp {{
        background-color: #0B0E14 !important;
        color: #F3F4F6 !important;
    }}
    
    /* Remove padding excessivo do topo do Streamlit */
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1000px !important;
    }}
    
    /* Header Institucional Superior */
    .header-wrapper {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 10px 20px 10px;
        background-color: #0B0E14;
        margin-bottom: 5px;
    }}
    
    .cefet-card {{
        background: #09203F;
        border: 1.5px solid #2563EB;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.4);
        border-radius: 14px;
        padding: 8px 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 130px;
        height: 75px;
    }}
    
    .cefet-card img {{
        max-height: 55px;
        max-width: 110px;
        object-fit: contain;
    }}
    
    .title-center {{
        text-align: center;
        flex-grow: 1;
        padding: 0 15px;
    }}
    
    .header-title-text {{
        color: #38BDF8 !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        letter-spacing: 1.2px;
        margin: 0;
        text-transform: uppercase;
        text-shadow: 0 0 18px rgba(56, 189, 248, 0.35);
    }}
    
    .header-subtitle-text {{
        color: #94A3B8 !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 1.05rem !important;
        margin-top: 4px;
        font-weight: 400;
    }}
    
    .fapemig-card img {{
        width: 78px;
        height: 78px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        border: 1px solid #38BDF8;
    }}
    
    /* Linha Divisória Neon */
    .neon-divider {{
        height: 2px;
        background: linear-gradient(90deg, #1E3A8A 0%, #EC4899 50%, #38BDF8 100%);
        box-shadow: 0 0 10px rgba(236, 72, 153, 0.5);
        margin-bottom: 30px;
    }}
    
    /* Card de Identificação "Estudante Ativo" */
    .student-container {{
        background-color: #161B26;
        border: 1px solid #242D3D;
        border-radius: 12px;
        padding: 14px 20px;
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 16px;
    }}
    
    .student-icon-box {{
        background-color: #2E2344;
        color: #A855F7;
        width: 44px;
        height: 44px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        flex-shrink: 0;
    }}
    
    .student-text-label {{
        color: #E2E8F0;
        font-size: 1.1rem;
        font-weight: 500;
        white-space: nowrap;
    }}
    
    /* Banner Verde de Sucesso */
    .success-alert-box {{
        background-color: rgba(16, 185, 129, 0.08);
        border: 1px solid #10B981;
        border-radius: 10px;
        padding: 12px 18px;
        color: #34D399;
        font-size: 1.05rem;
        font-weight: 500;
        margin-bottom: 25px;
    }}
    
    .success-alert-box strong {{
        color: #34D399;
    }}

    /* Estilização dos Balões de Chat e Borda Neon */
    [data-testid="stChatMessage"] {{
        background-color: transparent !important;
        padding: 8px 0px !important;
    }}

    /* Input do Chat na parte inferior */
    .stChatInputContainer {{
        background-color: #161B26 !important;
        border: 1px solid #242D3D !important;
        border-radius: 10px !important;
    }}
    
    /* Esconde elementos padrões do Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# RENDERIZAÇÃO DO CABEÇALHO (LOGO CEFET, TÍTULO E LOGO FAPEMIG)
# ==============================================================================
cefet_img_html = f'<img src="data:image/jpeg;base64,{cefet_b64}">' if cefet_b64 else '<b style="color:white;">CEFET-MG</b>'
fapemig_img_html = f'<img src="data:image/jpeg;base64,{fapemig_b64}">' if fapemig_b64 else '<b style="color:white;">FAPEMIG</b>'

st.markdown(f"""
<div class="header-wrapper">
    <div class="cefet-card">
        {cefet_img_html}
    </div>
    <div class="title-center">
        <h1 class="header-title-text">TRILHANDO O CAMINHO DO CÓDIGO</h1>
        <p class="header-subtitle-text">Projeto de Pesquisa e Extensão CEFET-MG & FAPEMIG</p>
    </div>
    <div class="fapemig-card">
        {fapemig_img_html}
    </div>
</div>
<div class="neon-divider"></div>
""", unsafe_allow_html=True)


# ==============================================================================
# FUNÇÕES DE CONFIGURAÇÃO E WEBHOOK
# ==============================================================================
def get_config(key: str, default: str = "") -> str:
    try:
        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.getenv(key, default)


DEFAULT_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe9ksgUqxMqSY8OUtDwmjwY187PPVguHBu7wHcUnOQA1eQTIg/formResponse"
DEFAULT_ENTRY_NOME = "entry.1009783107"
DEFAULT_ENTRY_PROMPT = "entry.1559793013"
DEFAULT_ENTRY_RESPOSTA = "entry.2041274618"

def send_to_google_forms(student_name: str, prompt: str, response: str):
    form_url = get_config("GOOGLE_FORM_URL", DEFAULT_FORM_URL)
    entry_nome = get_config("GOOGLE_ENTRY_NOME_ALUNO", DEFAULT_ENTRY_NOME)
    entry_prompt = get_config("GOOGLE_ENTRY_PROMPT_ALUNO", DEFAULT_ENTRY_PROMPT)
    entry_resposta = get_config("GOOGLE_ENTRY_RESPOSTA_IA", DEFAULT_ENTRY_RESPOSTA)

    def _post_request():
        if "SEU_FORM_ID_AQUI" in form_url or not form_url or not form_url.startswith("http"):
            return

        payload = {
            entry_nome: student_name,
            entry_prompt: prompt,
            entry_resposta: response
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        try:
            requests.post(form_url, data=payload, headers=headers, timeout=5)
        except Exception as e:
            print(f"[Webhook Forms Log] Erro ao enviar mineração de dados: {e}")

    threading.Thread(target=_post_request, daemon=True).start()


# Configuração da API Gemini
api_key = get_config("GEMINI_API_KEY")

if not api_key:
    with st.sidebar:
        st.header("🔑 Configuração da API")
        api_key = st.text_input("Gemini API Key", type="password", help="Insira sua chave da API do Google AI Studio.")
        st.info("Para salvar permanentemente, configure em `.env` ou em `.streamlit/secrets.toml`.")

if not api_key:
    st.error("⚠️ Chave de API do Gemini não encontrada! Por favor, insira a chave na barra lateral ou configure o ambiente.")
    st.stop()

genai.configure(api_key=api_key)


# ==============================================================================
# CONTROLE DE INTERFACE (UI) - "ESTUDANTE ATIVO"
# ==============================================================================
col_input, col_space = st.columns([1, 0.01])
with col_input:
    student_name = st.text_input(
        label="Estudante Ativo:",
        placeholder="Digite seu nome completo aqui para liberar o chat...",
        key="student_name_input"
    ).strip()

is_student_identified = bool(student_name)

if not is_student_identified:
    st.warning("🔒 Por favor, informe seu nome no campo 'Estudante Ativo' acima para liberar o chat.")
else:
    st.markdown(f"""
    <div class="success-alert-box">
        ✅ Bem-vindo(a), <strong>{student_name}</strong>! Seu chat está liberado.
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# CÉREBRO E PERSONALIDADE DO MODELO (GEMINI 1.5 FLASH)
# ==============================================================================
SYSTEM_INSTRUCTION = """
Você é o GEMINI-1.5-FLASH, assistente virtual do projeto "TRILHANDO O CAMINHO DO CÓDIGO".

SUA MISSÃO E REGRAS DE CONDUTA:
1. Sempre forneça a solução completa, clara e acompanhada do CÓDIGO COMPLETO e pronto para ser executado (em blocos de código ```python).
2. Explique detalhadamente o passo a passo de como o código funciona.
3. Ao responder sobre Flet ou Python, inclua todas as importações necessárias, declarações de função e event handlers.
4. Responda com tom didático, profissional, direto e acolhedor.
"""

GENERATION_CONFIG = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
}

@st.cache_resource
def get_generative_model():
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=GENERATION_CONFIG,
        system_instruction=SYSTEM_INSTRUCTION
    )

model = get_generative_model()

# ==============================================================================
# MEMÓRIA DE SESSÃO & EXIBIÇÃO DO CHAT
# ==============================================================================
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Renderiza as mensagens trocadas
for message in st.session_state.chat_session.history:
    if message.role == "user":
        with st.chat_message("user"):
            st.markdown(message.parts[0].text)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"**🤖 GEMINI-1.5-FLASH**")
            st.markdown(message.parts[0].text)

# Input de mensagens do usuário
prompt = st.chat_input(
    placeholder="Digite sua dúvida de Python ou peça um código em Flet...",
    disabled=not is_student_identified
)

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🤖 GEMINI-1.5-FLASH gerando a resposta..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                response_text = response.text
                st.markdown(f"**🤖 GEMINI-1.5-FLASH**")
                st.markdown(response_text)
                
                # MINERAÇÃO DE DADOS (WEBHOOK INVISÍVEL EM BACKGROUND)
                send_to_google_forms(
                    student_name=student_name,
                    prompt=prompt,
                    response=response_text
                )
            except Exception as e:
                st.error(f"Erro ao processar resposta da IA: {e}")
