# 🐍 Tutor Didático de Python & Flet (Chat Gemini 1.5 Flash)

Aplicação Web de Chat com Inteligência Artificial construída utilizando **Streamlit** e **google-generativeai** (Gemini 1.5 Flash). O app atua como um Tutor Didático que guia os alunos com dicas lógicas sem entregar código pronto e registra as interações de forma invisível via Webhook para o **Google Forms**.

---

## 🚀 Requisitos Atendidos

1. **Controle de Interface (UI)**: 
   - Campo `st.text_input` no topo solicitando o **Nome do Aluno**.
   - O chat (`st.chat_input`) fica **bloqueado/desativado** até que o aluno informe seu nome.

2. **Cérebro e Personalidade**:
   - Modelo configurado via `system_instruction` para atuar estritamente como um **tutor didático de Python e Flet**.
   - **Regra primordial**: Nunca entrega soluções ou códigos prontos; guia o aluno através de perguntas provocativas e dicas lógicas.

3. **Precisão Lógica**:
   - `temperature = 0.2` definida no `generation_config` para garantir respostas coerentes, objetivas e determinísticas.

4. **Memória de Sessão**:
   - Utilização de `model.start_chat(history=[])` salvo em `st.session_state` mantendo todo o contexto das trocas de mensagens na sessão atual.

5. **Mineração de Dados (Webhook Invisível)**:
   - Função executada em **Background Thread** com `requests.post`.
   - Ao gerar cada resposta, envia automaticamente `Nome do Aluno`, `Prompt do Aluno` e `Resposta da IA` para o Google Forms sem travar ou atrasar a interface gráfica.

---

## 📦 Instalação e Execução Local

### 1. Clone ou acesse o repositório
```bash
cd "Chat Gemini"
```

### 2. Crie e ative um ambiente virtual (Opcional, mas recomendado)
```bash
python -m venv venv
# No Windows PowerShell:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração das Variáveis de Ambiente
Crie um arquivo `.env` baseado no `.env.example` ou exporte no seu terminal:

```env
GEMINI_API_KEY=sua_chave_aqui
GOOGLE_FORM_URL=https://docs.google.com/forms/d/e/SEU_FORM_ID/formResponse
GOOGLE_ENTRY_NOME_ALUNO=entry.1000000001
GOOGLE_ENTRY_PROMPT_ALUNO=entry.1000000002
GOOGLE_ENTRY_RESPOSTA_IA=entry.1000000003
```

> **Dica para obter os IDs do Google Forms (`entry.XXXXXX`)**:
> 1. Abra seu formulário no Google Forms.
> 2. Clique nos 3 pontinhos (Menu) -> **Obter link preenchido previamente** (*Get pre-filled link*).
> 3. Preencha campos de teste, clique em **Obter link** e copie o link gerado.
> 4. No link copiado você verá parâmetros como `?entry.12345678=...`. Esses são os seus IDs!

### 5. Executar a aplicação
```bash
streamlit run app.py
```

---

## ☁️ Deploy no Streamlit Cloud

1. Suba esta pasta para um repositório no **GitHub**.
2. Acesse [share.streamlit.io](https://share.streamlit.io/) e selecione o repositório e o arquivo `app.py`.
3. Vá em **Advanced Settings** -> **Secrets** e adicione suas chaves:

```toml
GEMINI_API_KEY = "sua_chave_gemini_aqui"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/SEU_FORM_ID/formResponse"
GOOGLE_ENTRY_NOME_ALUNO = "entry.1000000001"
GOOGLE_ENTRY_PROMPT_ALUNO = "entry.1000000002"
GOOGLE_ENTRY_RESPOSTA_IA = "entry.1000000003"
```
4. Clique em **Deploy**! 🚀
