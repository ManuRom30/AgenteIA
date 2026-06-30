# Propuesta de Infraestructura - Agente IA Lafayette

## Fase 1: MVP (Semanas 1-3)

### Objetivo
App funcional con conocimiento base, desplegada y accesible por URL.

```
[Streamlit Cloud / Railway]
         |
   [App Python]
    /    |    \
[GPT]  [Chroma]  [Tavily]
        |
  [/data/*.txt, *.json]
  (conocimiento interno)
```

### Componentes
- **Hosting**: Streamlit Community Cloud (gratis, conecta directo a GitHub)
- **Almacenamiento de conocimiento**: Archivos en el repo (JSON/TXT con QA pairs)
- **Vector DB**: ChromaDB en memoria (se reconstruye al deploy)
- **Secretos**: Streamlit Secrets (variables de entorno seguras)

### Limitaciones MVP
- Sin autenticacion (o password simple via Streamlit)
- ChromaDB se reinicia en cada deploy (aceptable para <100 docs)
- Sin historial persistente de conversaciones

---

## Fase 2: Produccion (Semanas 4-6)

### Objetivo
Estabilizar, agregar autenticacion, persistir datos.

```
[Streamlit Cloud / Railway]
         |
   [App Python]
    /    |    \     \
[GPT]  [Pinecone] [Tavily] [Supabase]
                              |
                     [Auth + Chat History]
```

### Mejoras
- **Vector DB**: Migrar a Pinecone (persistente, no se pierde en redeploy)
- **Auth**: Streamlit-authenticator o Supabase Auth
- **Historial**: Guardar conversaciones en Supabase (PostgreSQL)
- **Analytics**: Dashboard basico de uso (preguntas frecuentes, satisfaccion)

---

## Fase 3: Escala (Mes 2+)

### Objetivo
Multi-tenant, administracion, mejora continua.

```
[Custom Domain]
       |
[Streamlit / React Frontend]
       |
[FastAPI Backend]
    /    |    \      \
[GPT] [Pinecone] [Tavily] [Supabase]
                              |
                  [Auth + History + Admin]
```

### Mejoras
- **Backend separado** (FastAPI) si se necesita mas control
- **Panel admin** para Lafayette (subir docs, ver metricas)
- **Multi-modelo**: Usar GPT-4o para preguntas complejas, mini para simples
- **Cache**: Redis para respuestas frecuentes (reduce costos)
- **Custom domain**: lafayette-ai.com o similar

---

## Estrategia de Deploy

### Opcion A: Streamlit Cloud (Recomendada para MVP)
- **Pro**: Gratis, zero-config, conecta directo al repo GitHub
- **Con**: Limitado en customizacion, cold starts
- **Setup**: Push al repo -> deploy automatico

### Opcion B: Railway
- **Pro**: Mas control, sin cold starts, $5/mes
- **Con**: Requiere Dockerfile o Procfile
- **Setup**: Conectar repo -> configurar build

### Opcion C: Render
- **Pro**: Similar a Railway, tier gratis disponible
- **Con**: Cold starts en tier gratis (30s+)

---

## Variables de Entorno Requeridas

```
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
# Fase 2+
PINECONE_API_KEY=...
SUPABASE_URL=...
SUPABASE_KEY=...
```

---

## Estructura de Proyecto Propuesta

```
AgenteIA/
├── .claude/              # Documentacion del proyecto
├── .streamlit/
│   └── config.toml      # Config UI Streamlit
├── app.py               # Entry point Streamlit
├── src/
│   ├── agent.py         # Logica del agente (LangChain)
│   ├── vectorstore.py   # Manejo de ChromaDB/Pinecone
│   ├── search.py        # Busqueda externa (Tavily)
│   └── prompts.py       # System prompts y templates
├── data/
│   ├── incoterms.json   # Conocimiento: Incoterms
│   ├── documentacion.json
│   ├── flujo_cambiario.json
│   └── riesgos.json
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Seguridad

- API keys NUNCA en el codigo (usar .env / secrets)
- .gitignore incluye: .env, __pycache__, chroma_db/
- Rate limiting basico en Fase 2
- Input sanitization (evitar prompt injection)
