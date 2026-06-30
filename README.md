# AgenteIA - Asistente de Exportacion Lafayette

Chatbot de IA que asesora a clientes de Lafayette sobre exportacion de textiles y confecciones.

## Funcionalidades

- Consultas sobre Incoterms (EXW, FOB, CIF, CPT, CIP, DAP, DDP)
- Costos de exportacion y matrices de precio
- Documentacion requerida (factura, packing list, DEX, proforma)
- Flujo cambiario y medios de pago internacionales
- Busqueda web de aranceles y normativa actualizada

## Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT 5.4 mini
- **RAG**: LangChain + ChromaDB
- **Busqueda web**: Tavily API

## Setup local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env con tus API keys
streamlit run app.py
```

## Deploy en Streamlit Cloud

1. Push el repo a GitHub
2. Conectar en share.streamlit.io
3. Configurar secrets (OPENAI_API_KEY, TAVILY_API_KEY)
4. Deploy automatico

## Variables de entorno

| Variable | Requerida | Descripcion |
|----------|-----------|-------------|
| OPENAI_API_KEY | Si | API key de OpenAI |
| TAVILY_API_KEY | No | API key de Tavily para busqueda web |
