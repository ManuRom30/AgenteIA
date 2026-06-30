# Plan de Trabajo - Agente IA Lafayette

## Fase 1: MVP Funcional (Semanas 1-3)

### Sprint 1 (Semana 1): Setup + Base de Conocimiento
- [ ] Configurar estructura del proyecto
- [ ] Crear requirements.txt y .gitignore
- [ ] Procesar documentos de conocimiento (Preguntas comex) a formato JSON
- [ ] Implementar vector store con ChromaDB
- [ ] Crear embeddings del conocimiento base
- [ ] Test: verificar que retrieval funciona correctamente

### Sprint 2 (Semana 2): Agente + Chat
- [ ] Implementar agente con LangChain + OpenAI
- [ ] Disenar system prompt (personalidad: asesor experto Lafayette)
- [ ] Integrar RAG (retrieval + generacion)
- [ ] Crear interfaz Streamlit con st.chat_message
- [ ] Integrar busqueda web (Tavily) para consultas externas
- [ ] Test: conversacion completa end-to-end

### Sprint 3 (Semana 3): Polish + Deploy
- [ ] Ajustar prompts basado en pruebas
- [ ] Agregar manejo de errores y fallbacks
- [ ] Configurar Streamlit Cloud o Railway
- [ ] Deploy a produccion
- [ ] Pruebas con usuarios internos Lafayette
- [ ] Documentar uso para equipo Lafayette

---

## Fase 2: Estabilizacion (Semanas 4-6)
- [ ] Migrar a Pinecone (persistencia)
- [ ] Agregar autenticacion basica
- [ ] Implementar historial de conversaciones
- [ ] Dashboard de metricas basico
- [ ] Feedback loop: mejorar respuestas basado en uso real

---

## Fase 3: Escala (Mes 2+)
- [ ] Evaluar necesidad de backend separado (FastAPI)
- [ ] Panel admin para gestionar conocimiento
- [ ] Multi-modelo (GPT-4o para complejo, mini para simple)
- [ ] Custom domain
- [ ] Integracion con sistemas internos Lafayette

---

## Criterios de Exito MVP
1. El agente responde correctamente al 80%+ de las preguntas del documento "Preguntas comex"
2. Tiempo de respuesta < 5 segundos
3. Al menos 3 clientes Lafayette pueden usarlo sin soporte
4. Costo mensual < $30 USD

---

## Riesgos y Mitigacion

| Riesgo | Probabilidad | Impacto | Mitigacion |
|--------|-------------|---------|-----------|
| Respuestas incorrectas del LLM | Media | Alto | RAG + system prompt estricto + disclaimer |
| Costos OpenAI se disparan | Baja | Medio | Rate limiting + GPT-4o-mini + cache |
| Streamlit no escala | Media | Medio | Plan B: migrar a Railway/Render |
| Conocimiento desactualizado | Alta | Medio | Proceso de actualizacion periodica |
