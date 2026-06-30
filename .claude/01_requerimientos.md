# Requerimientos del Proyecto - Agente IA Lafayette

## Cliente
Lafayette - Empresa colombiana del sector textil y confecciones

## Objetivo
Desarrollar un asistente virtual (chatbot) que permita a los clientes de Lafayette resolver dudas sobre exportacion de textiles y confecciones, integrando conocimiento interno y fuentes externas.

---

## Requerimientos Funcionales

### RF-01: Chat conversacional
- Interfaz tipo chat accesible desde navegador web
- Respuestas claras, simples y con ejemplos aplicados
- Capacidad de hacer preguntas de seguimiento al usuario

### RF-02: Modulos de conocimiento
El agente debe resolver preguntas en estas areas:
1. **Costos e Incoterms** - EXW, FOB, CIF, DDP, CPT, CIP. Calculo de costos, matrices, costos ocultos
2. **Documentacion de exportacion** - Factura comercial, packing list, proforma, DEX, RUT, coherencia documental
3. **Flujo cambiario y pagos** - TRM, medios de pago internacionales, cartas de credito, reintegro de divisas
4. **Riesgos y buenas practicas** - Riesgo cambiario, cobertura, verificacion de clientes, errores comunes

### RF-03: Busqueda externa
- Consulta de aranceles actualizados
- Regulacion por pais destino
- Tratados comerciales (TLC)
- Restricciones de exportacion

### RF-04: Base de conocimiento interna
- Alimentada con contenido de mentorias Lafayette
- Reglas criticas del negocio (ej: packing list debe coincidir EXACTAMENTE con factura)
- Flujos reales de proceso (ficha tecnica -> proforma -> factura -> packing list -> DEX)

---

## Requerimientos No Funcionales

### RNF-01: Despliegue rapido
- MVP funcional en semanas, no meses
- Interfaz lista para demos con clientes reales

### RNF-02: Escalabilidad
- Soporte para multiples clientes simultaneos
- Capacidad de agregar nuevos modulos de conocimiento

### RNF-03: Seguridad
- No exponer informacion sensible de Lafayette
- Control de acceso basico (al menos autenticacion simple)

### RNF-04: Mantenibilidad
- Facil actualizacion de la base de conocimiento
- Logs de conversaciones para mejora continua

---

## Tipos de Usuario
- **Clientes principiantes**: Primera exportacion, necesitan guia paso a paso
- **Clientes con experiencia**: Consultas especificas sobre costos, normativa, Incoterms avanzados
- **Equipo interno Lafayette**: Administracion del agente y contenido

---

## Preguntas Frecuentes Identificadas (Muestra)
- "Que Incoterm me conviene para exportar prendas?"
- "Como calcular el costo de exportacion de una prenda?"
- "Que documentos necesito para exportar ropa?"
- "Como funciona el pago en una exportacion?"
- "Que medio de pago es mas seguro para exportar?"
- "Mi cliente me quiere pagar en dolares, que hago?"
