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

# Resolução dinâmica e à prova de falhas para caminhos de imagem (Local e Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

def get_base64_image(file_name: str) -> str:
    possible_paths = [
        os.path.join(BASE_DIR, "assets", file_name),
        os.path.join(ROOT_DIR, "assets", file_name),
        os.path.join(ROOT_DIR, "arquivos-trilhando", "Imagens", file_name),
        os.path.join(os.getcwd(), "assets", file_name),
        os.path.join(os.getcwd(), "Chat Gemini", "assets", file_name),
        file_name
    ]
    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode()
            except Exception:
                pass
    return ""

cefet_b64 = get_base64_image("logo-cefet.jpg")
fapemig_b64 = get_base64_image("logo-fapemig.jpg")

# CSS para réplica 100% fiel ao design da imagem de exemplo
st.markdown("""
<meta name="google" content="notranslate">
<style>
    /* Prevenção contra travamento do Google Tradutor no React DOM */
    .stApp {
        translate: no !important;
        background-color: #0B0E14 !important;
        color: #F3F4F6 !important;
    }
    
    /* Remove espaçamentos extras do topo */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 950px !important;
    }
    
    /* Cabeçalho Institucional */
    .header-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 0px 20px 0px;
        background-color: #0B0E14;
    }
    
    .cefet-card-box {
        background: #09203F;
        border: 1.5px solid #2563EB;
        box-shadow: 0 0 16px rgba(37, 99, 235, 0.45);
        border-radius: 14px;
        padding: 6px 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 140px;
        height: 75px;
    }
    
    .cefet-card-box img {
        max-height: 55px;
        max-width: 120px;
        object-fit: contain;
    }
    
    .title-center-box {
        text-align: center;
        flex-grow: 1;
        padding: 0 20px;
    }
    
    .header-title-text {
        color: #38BDF8 !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        letter-spacing: 1.5px;
        margin: 0;
        text-transform: uppercase;
        text-shadow: 0 0 18px rgba(56, 189, 248, 0.35);
    }
    
    .header-subtitle-text {
        color: #94A3B8 !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 1.05rem !important;
        margin-top: 4px;
        font-weight: 400;
    }
    
    .fapemig-card-box img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 0 16px rgba(56, 189, 248, 0.45);
        border: 1.5px solid #38BDF8;
    }
    
    /* Linha Divisória Neon */
    .neon-divider {
        height: 2px;
        background: linear-gradient(90deg, #1E3A8A 0%, #EC4899 50%, #38BDF8 100%);
        box-shadow: 0 0 10px rgba(236, 72, 153, 0.5);
        margin-bottom: 25px;
    }
    
    /* Estilização do Campo Estudante Ativo */
    div[data-testid="stTextInput"] > label {
        color: #94A3B8 !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;
    }
    
    div[data-testid="stTextInput"] input {
        background-color: #1E2638 !important;
        color: #FFFFFF !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        font-size: 1rem !important;
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3) !important;
    }
    
    /* Banner Verde de Sucesso */
    .success-alert-box {
        background-color: rgba(16, 185, 129, 0.08);
        border: 1.5px solid #10B981;
        border-radius: 10px;
        padding: 12px 20px;
        color: #34D399;
        font-size: 1.05rem;
        font-weight: 500;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.15);
    }
    
    .success-alert-box strong {
        color: #34D399;
    }

    /* Balões de Chat e Input inferior */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        padding: 8px 0px !important;
    }

    .stChatInputContainer {
        background-color: #161B26 !important;
        border: 1px solid #242D3D !important;
        border-radius: 10px !important;
    }
    
    /* Ocultar elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# RENDERIZAÇÃO DO CABEÇALHO (LOGO CEFET, TÍTULO E LOGO FAPEMIG)
# ==============================================================================
cefet_img_html = f'<img src="data:image/jpeg;base64,{cefet_b64}">' if cefet_b64 else '<b style="color:white;">CEFET-MG</b>'
fapemig_img_html = f'<img src="data:image/jpeg;base64,{fapemig_b64}">' if fapemig_b64 else '<b style="color:white;">FAPEMIG</b>'

st.markdown(f"""
<div class="header-wrapper">
    <div class="cefet-card-box">
        {cefet_img_html}
    </div>
    <div class="title-center-box">
        <h1 class="header-title-text">TRILHANDO O CAMINHO DO CÓDIGO</h1>
        <p class="header-subtitle-text">Projeto de Pesquisa e Extensão CEFET-MG & FAPEMIG</p>
    </div>
    <div class="fapemig-card-box">
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
# CÉREBRO E PERSONALIDADE DO MODELO (GEMINI 3.8 / FLASH)
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
    candidatos = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-1.5-flash", "gemini-2.5-flash"]
    for m_name in candidatos:
        try:
            return genai.GenerativeModel(
                model_name=m_name,
                generation_config=GENERATION_CONFIG,
                system_instruction=SYSTEM_INSTRUCTION
            )
        except Exception:
            continue
    return genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        generation_config=GENERATION_CONFIG,
        system_instruction=SYSTEM_INSTRUCTION
    )

model = get_generative_model()

# ==============================================================================
# MEMÓRIA DE SESSÃO & EXIBIÇÃO DO CHAT
# ==============================================================================
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

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
        with st.spinner("🤖 GEMINI IA gerando a resposta..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                response_text = response.text
            except Exception as first_err:
                try:
                    fallback_model = genai.GenerativeModel(
                        model_name="gemini-3.8-flash",
                        generation_config=GENERATION_CONFIG,
                        system_instruction=SYSTEM_INSTRUCTION
                    )
                    st.session_state.chat_session = fallback_model.start_chat(history=[])
                    response = st.session_state.chat_session.send_message(prompt)
                    response_text = response.text
                except Exception as final_err:
                    st.error(f"Erro ao processar resposta da IA: {final_err}")
                    response_text = None

            if response_text:
                st.markdown(f"**🤖 GEMINI-1.5-FLASH**")
                st.markdown(response_text)
                
                # MINERAÇÃO DE DADOS (WEBHOOK INVISÍVEL EM BACKGROUND)
                send_to_google_forms(
                    student_name=student_name,
                    prompt=prompt,
                    response=response_text
                )
