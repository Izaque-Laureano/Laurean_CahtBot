import sqlite3
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

# Configuração da API Groq (usada com LangChain)
api_base = "https://api.groq.com/openai/v1"
api_key = "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"

chat = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    openai_api_base=api_base,
    openai_api_key=api_key,
)

# Configuração do banco de dados SQLite
conn = sqlite3.connect("chatbot_data.db")
cursor = conn.cursor()

# Criação das tabelas, se não existirem
cursor.execute("""
CREATE TABLE IF NOT EXISTS facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    info TEXT UNIQUE
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    preference TEXT UNIQUE,
    value TEXT
)
""")
conn.commit()

# Função para armazenar informações factuais
def store_fact(info):
    try:
        cursor.execute("INSERT INTO facts (info) VALUES (?)", (info,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Evita duplicação

# Função para armazenar ou atualizar preferências
def store_preference(pref, value):
    cursor.execute("INSERT OR REPLACE INTO preferences (preference, value) VALUES (?, ?)", (pref, value))
    conn.commit()

# Função para recuperar fatos armazenados
def retrieve_facts():
    cursor.execute("SELECT info FROM facts")
    return [row[0] for row in cursor.fetchall()]

# Função para recuperar preferências
def retrieve_preferences():
    cursor.execute("SELECT preference, value FROM preferences")
    return {row[0]: row[1] for row in cursor.fetchall()}

# Interface do chatbot no Streamlit
st.title("Laurean Chat")
st.subheader("Converse com o Laurean Chat e ensine novas informações!")

# Inicialização do estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="Você é um assistente útil e amigável."),
        AIMessage(content="Olá! Como posso ajudar você hoje?")
    ]

# Recuperar preferências e personalizar respostas
preferences = retrieve_preferences()
tone = preferences.get("tone", "informal")  # Padrão: informal

# Exibir mensagens anteriores
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# Entrada do usuário
user_input = st.chat_input("Digite sua mensagem...")
if user_input:
    # Exibir mensagem do usuário na interface
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.chat_message("user").markdown(user_input)

    # Verificar preferências ou fatos no texto do usuário
    if "lembre-se" in user_input.lower():
        info = user_input.replace("lembre-se de que", "").strip()
        store_fact(info)
        response_content = f"Entendido. Vou me lembrar de que: {info}."
        st.session_state.messages.append(AIMessage(content=response_content))
    elif "prefiro" in user_input.lower():
        pref = "tone"
        value = "formal" if "formal" in user_input.lower() else "informal"
        store_preference(pref, value)
        response_content = f"Entendido. Vou usar um tom {value} nas respostas."
        st.session_state.messages.append(AIMessage(content=response_content))
    else:
        # Gerar resposta usando LangChain com a API da Groq
        try:
            response = chat(st.session_state.messages)
            response_content = response.content
            st.session_state.messages.append(AIMessage(content=response_content))
        except Exception as e:
            response_content = f"Erro ao gerar resposta: {e}"
            st.session_state.messages.append(AIMessage(content=response_content))

    # Exibir a resposta na interface
    st.chat_message("assistant").markdown(response_content)
