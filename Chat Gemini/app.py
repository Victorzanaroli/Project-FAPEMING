import os
import threading
import requests
from datetime import datetime
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env local, se existir
load_dotenv()

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA DO STREAMLIT & DESIGN INSTITUCIONAL (CEFET / FAPEMIG)
# ==============================================================================
st.set_page_config(
    page_title="Tutor Didático de Python",
    page_icon="🐍",
    layout="centered"
)

# Custom CSS para aplicar cores institucionais (Azul Marinho CEFET & Detalhes FAPEMIG)
st.markdown("""
<style>
    /* Estilização da página principal */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Títulos e Cabeçalho */
    .main-header-title {
        color: #0F2C59;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .main-header-subtitle {
        color: #475569;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 1.05rem;
        text-align: center;
        margin-top: 4px;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Borda e destaques institucionais */
    .header-divider {
        height: 4px;
        background: linear-gradient(90deg, #0F2C59 0%, #C8102E 50%, #0F2C59 100%);
        border-radius: 2px;
        margin-bottom: 25px;
    }

    /* Estilização de botões e entradas */
    .stButton>button {
        background-color: #0F2C59;
        color: white;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background-color: #1E3A8A;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Exibição dos Logos do CEFET e da FAPEMIG no cabeçalho
col_cefet, col_title, col_fapemig = st.columns([1.2, 3.6, 1.2])

# Caminhos dos logos (suporta caminho local assets e fallback)
cefet_logo_path = "assets/logo-cefet.jpg" if os.path.exists("assets/logo-cefet.jpg") else "../arquivos-trilhando/Imagens/logo-cefet.jpg"
fapemig_logo_path = "assets/logo-fapemig.jpg" if os.path.exists("assets/logo-fapemig.jpg") else "../arquivos-trilhando/Imagens/logo-fapemig.jpg"

with col_cefet:
    if os.path.exists(cefet_logo_path):
        st.image(cefet_logo_path, use_container_width=True)

with col_title:
    st.markdown('<h1 class="main-header-title">Tutor Didático de Python</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-header-subtitle">Projeto de Pesquisa e Extensão CEFET-MG & FAPEMIG</p>', unsafe_allow_html=True)

with col_fapemig:
    if os.path.exists(fapemig_logo_path):
        st.image(fapemig_logo_path, use_container_width=True)

# Divisor estilizado nas cores institucionais
st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)


# ==============================================================================
# FUNÇÃO AUXILIAR PARA RECUPERAR CONFIGURAÇÕES (SECRETS / ENV)
# ==============================================================================
def get_config(key: str, default: str = "") -> str:
    """Busca a chave primeiro em st.secrets (Streamlit Cloud) e depois em os.getenv."""
    try:
        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.getenv(key, default)


# ==============================================================================
# CONFIGURAÇÕES DE MINERAÇÃO DE DADOS (GOOGLE FORMS WEBHOOK)
# ==============================================================================
DEFAULT_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe9ksgUqxMqSY8OUtDwmjwY187PPVguHBu7wHcUnOQA1eQTIg/formResponse"
DEFAULT_ENTRY_NOME = "entry.1009783107"
DEFAULT_ENTRY_PROMPT = "entry.1559793013"
DEFAULT_ENTRY_RESPOSTA = "entry.2041274618"
DEFAULT_ENTRY_DATA = "entry.1000000004"


def send_to_google_forms(student_name: str, prompt: str, response: str):
    """
    Função em segundo plano (Background Thread) para disparar um POST para o Google Forms.
    Executa de forma não-bloqueante (invisível ao usuário) usando a biblioteca requests.
    """
    form_url = get_config("GOOGLE_FORM_URL", DEFAULT_FORM_URL)
    entry_nome = get_config("GOOGLE_ENTRY_NOME_ALUNO", DEFAULT_ENTRY_NOME)
    entry_prompt = get_config("GOOGLE_ENTRY_PROMPT_ALUNO", DEFAULT_ENTRY_PROMPT)
    entry_resposta = get_config("GOOGLE_ENTRY_RESPOSTA_IA", DEFAULT_ENTRY_RESPOSTA)
    entry_data = get_config("GOOGLE_ENTRY_DATA_HORA", DEFAULT_ENTRY_DATA)

    def _post_request():
        if "SEU_FORM_ID_AQUI" in form_url or not form_url or not form_url.startswith("http"):
            return

        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        payload = {
            entry_nome: student_name,
            entry_prompt: prompt,
            entry_resposta: response
        }
        
        if entry_data and "1000000004" not in entry_data:
            payload[entry_data] = now_str

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        try:
            requests.post(form_url, data=payload, headers=headers, timeout=5)
        except Exception as e:
            print(f"[Webhook Forms Log] Erro ao enviar mineração de dados: {e}")

    threading.Thread(target=_post_request, daemon=True).start()


# ==============================================================================
# CONFIGURAÇÃO DA CHAVE DA API GEMINI
# ==============================================================================
api_key = get_config("GEMINI_API_KEY")

if not api_key:
    with st.sidebar:
        st.header("🔑 Configuração da API")
        api_key = st.text_input("Gemini API Key", type="password", help="Insira sua chave da API do Google AI Studio.")
        st.info("Para salvar permanentemente, configure em `.env` ou em `.streamlit/secrets.toml`.")

if not api_key:
    st.error("⚠️ Chave de API do Gemini não encontrada! Por favor, insira a chave na barra lateral ou configure o ambiente.")
    st.stop()

# Configura a biblioteca google-generativeai
genai.configure(api_key=api_key)

# ==============================================================================
# CONTROLE DE INTERFACE (UI) - IDENTIFICAÇÃO DO ALUNO
# ==============================================================================
st.subheader("👤 Identificação do Aluno")
student_name = st.text_input(
    label="Nome do Aluno:",
    placeholder="Digite seu nome completo aqui para liberar o chat...",
    key="student_name_input"
).strip()

is_student_identified = bool(student_name)

if not is_student_identified:
    st.warning("🔒 Por favor, informe seu nome acima para ativar o Tutor Virtual.")
else:
    st.success(f"Bem-vindo(a), **{student_name}**! Seu chat está liberado.")

st.markdown("---")

# ==============================================================================
# CÉREBRO E PERSONALIDADE DO MODELO (GEMINI 1.5 FLASH)
# ==============================================================================
SYSTEM_INSTRUCTION = """
Você é o Tutor Didático de Python, um assistente virtual especialista em linguagem Python, lógica de programação e desenvolvimento de interfaces gráficas e móveis com o framework Flet.

SUA MISSÃO E REGRAS DE RESPOSTA:
1. Sempre forneça respostas claras, bem estruturadas e acompanhadas de CÓDIGO COMPLETO, limpo e pronto para ser executado (utilizando blocos de código markdown com ```python).
2. Explique detalhadamente como o código funciona, passo a passo, incluindo as melhores práticas de desenvolvimento.
3. Quando o aluno solicitar interfaces com Flet ou programas em Python, inclua todos os imports necessários, estruturas de função e exemplos práticos.
4. Mantenha um tom didático, encorajador, profissional e acolhedor.
"""

GENERATION_CONFIG = {
    "temperature": 0.2, # Respostas determinísticas e precisas
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
# MEMÓRIA DE SESSÃO & HISTÓRICO DE CHAT
# ==============================================================================
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# ==============================================================================
# PROCESSAMENTO DE MENSAGENS (CHAT INPUT)
# ==============================================================================
prompt = st.chat_input(
    placeholder="Digite sua dúvida de Python ou peça um código em Flet...",
    disabled=not is_student_identified
)

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("O Tutor está gerando a resposta e o código..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                response_text = response.text
                st.markdown(response_text)
                
                # MINERAÇÃO DE DADOS (WEBHOOK INVISÍVEL EM BACKGROUND)
                send_to_google_forms(
                    student_name=student_name,
                    prompt=prompt,
                    response=response_text
                )
            except Exception as e:
                st.error(f"Erro ao processar resposta da IA: {e}")
