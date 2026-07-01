import streamlit as st
from dotenv import load_dotenv

from src.agent import get_response
from src.vectorstore import get_vectorstore

load_dotenv()

st.set_page_config(
    page_title="ComexIa - Asistente de Exportacion By Lafayette",
    page_icon="🧵",
    layout="centered",
)


@st.cache_resource
def init_resources():
    from langchain_openai import ChatOpenAI

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )
    llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0.3)
    return retriever, llm


retriever, llm = init_resources()

# --- Sidebar ---
with st.sidebar:
    st.title("Hola Soy ComexIA By Lafayette")
    st.caption("Tu asistente de Exportacion")
    st.divider()
    st.markdown("**Puedo ayudarte con:**")
    st.markdown("""
    - 📦 Incoterms y logistica
    - 💰 Costos de exportacion
    - 📄 Documentacion requerida
    - 💱 Flujo cambiario y pagos
    - ⚠️ Riesgos y buenas practicas
    """)
    st.divider()
    st.markdown("**Preguntas sugeridas:**")
    suggestions = [
        "¿Que Incoterm me conviene para mi primera exportacion?",
        "¿Que documentos necesito para exportar ropa?",
        "¿Como calculo el costo de exportacion?",
        "¿Que medio de pago es mas seguro?",
    ]
    for s in suggestions:
        if st.button(s, key=s, use_container_width=True):
            st.session_state["suggested_question"] = s

    st.divider()
    st.caption("Powered by Lafayette + IA")

# --- Main Chat ---
st.title("Asistente de Exportacion")
st.caption("Resuelve tus dudas sobre exportacion de textiles y confecciones")

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(
            "¡Hola soy ComexIA! Soy el asistente de exportacion de Lafayette. "
            "Estoy aqui para ayudarte con dudas sobre Incoterms, costos, "
            "documentacion, pagos internacionales y mas. "
            "\n\n¿En que puedo ayudarte hoy?"
        )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Escribe tu pregunta sobre exportacion...")

if "suggested_question" in st.session_state:
    prompt = st.session_state.pop("suggested_question")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consultando..."):
            response = get_response(
                query=prompt,
                chat_history=st.session_state.messages[:-1],
                retriever=retriever,
                llm=llm,
            )
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
