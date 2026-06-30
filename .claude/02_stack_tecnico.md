# Stack Tecnico - Agente IA Lafayette

## Decision: Despliegue rapido con Streamlit + GPT

Prioridad: tener un MVP funcional rapidamente que clientes puedan usar.

---

## Stack Seleccionado

| Capa | Tecnologia | Justificacion |
|------|-----------|---------------|
| Frontend | **Streamlit** | Despliegue inmediato, sin necesidad de frontend separado, UI de chat nativa |
| LLM | **OpenAI GPT-4o / GPT-4o-mini** | Mejor relacion costo/calidad para espanol, tool calling nativo |
| Base vectorial | **ChromaDB** (local) o **Pinecone** (cloud) | ChromaDB para MVP, Pinecone si escala |
| Embeddings | **OpenAI text-embedding-3-small** | Compatible con el ecosistema, buen rendimiento en espanol |
| Framework RAG | **LangChain** | Orquestacion de retrieval + LLM, integracion con OpenAI |
| Busqueda externa | **Tavily API** o **SerpAPI** | Para consultas de aranceles, normativa en tiempo real |
| Deploy | **Streamlit Cloud** (gratis) o **Railway/Render** | Zero-config, dominio publico inmediato |
| Versionamiento | **GitHub** (ya configurado) | Repo: ManuRom30/AgenteIA |

---

## Arquitectura de Alto Nivel

```
[Cliente Browser]
       |
[Streamlit App]
       |
[LangChain Agent]
    /        \
[Vector Store]  [Web Search]
(ChromaDB)      (Tavily/Serp)
    |
[Documentos Lafayette]
(PDFs, textos, QA pairs)
```

---

## Modelo de Costos Estimado (MVP)

| Servicio | Costo mensual estimado |
|----------|----------------------|
| OpenAI GPT-4o-mini | ~$5-20 USD (dependiendo uso) |
| OpenAI Embeddings | ~$1-5 USD |
| Streamlit Cloud | Gratis (tier basico) |
| Tavily API | Gratis (1000 queries/mes) |
| **Total MVP** | **~$10-30 USD/mes** |

---

## Alternativas Consideradas

### Frontend
- **React**: Mas flexible pero requiere mas tiempo de desarrollo
- **Gradio**: Similar a Streamlit pero menos features de chat
- **Streamlit** (elegido): Chat nativo, deploy en 1 click, ideal para MVP

### LLM
- **GPT-4o**: Mejor calidad, mas caro (~$5/1M input tokens)
- **GPT-4o-mini** (recomendado para MVP): 90% de calidad, 10x mas barato
- **Gemini**: Buena alternativa, pero ecosistema menos maduro para RAG

### Base Vectorial
- **Pinecone**: Managed, escala bien, tiene costo
- **ChromaDB** (elegido para MVP): Open source, corre local, zero cost
- **Supabase pgvector**: Buena opcion si se necesita SQL tambien

---

## Dependencias Python (requirements.txt)

```
streamlit>=1.28
openai>=1.0
langchain>=0.1
langchain-openai>=0.1
chromadb>=0.4
python-docx>=0.8
tiktoken>=0.5
tavily-python>=0.3
```
