# Recomendación — Employee Onboarding Assistant

## Caso de uso

El Employee Onboarding Assistant de Bridge SA es un agente conversacional diseñado para guiar y resolver dudas de los nuevos empleados de los departamentos de Engineering, Sales y Operations durante sus primeros 30 días de integración, cubriendo accesos técnicos (GitHub, Slack, Notion, HubSpot) y flujos de políticas internas (bajas, modalidades remotas cross-border). El asistente **no** proporciona soporte a clientes o participantes externos de los programas formativos, no interviene en la gestión académica de las cohortes, y tiene estrictamente prohibido emitir consejos financieros o desvelar información salarial o privada del equipo. Se apoya en FAQs y documentación interna.

## Modelo recomendado para producción

El modelo recomendado para el **chat en tiempo real** es **`gemini-3.1-flash-lite`**. Los resultados de este benchmark demuestran que es la opción más equilibrada: ofrece una latencia media sensiblemente inferior (1366 ms frente a 1449 ms) y optimiza el consumo de tokens de salida. A nivel cualitativo, demostró una robustez superior a la de su hermano mayor en el aislamiento de contextos de usuario (`p6`), evitando el uso de jergas cruzadas entre departamentos y manteniendo un tono corporativo óptimo para la experiencia del empleado nuevo.

## Modelo alternativo (opcional)

Se sugiere considerar **`gemini-3.5-flash`** como modelo alternativo enfocado exclusivamente a la **resolución de consultas de negocio complejas o ambiguas** en flujos de backend asíncronos (como el análisis profundo de planes de carrera o entrenamiento de ventas). En el caso `p4`, este modelo evidenció una mayor capacidad de inferencia al conectar el cronograma interno e inyectar proactivamente actividades del Día 3 (*shadowing* comercial), aportando una riqueza informativa que el modelo Lite omitió.

## Trade-off principal

Al seleccionar el modelo Lite para producción, ganamos de manera inmediata **velocidad de respuesta (~83 ms más rápido por interacción de media)** y una drástica **reducción de costes operativos directos** debido a la tarificación más económica de la familia Lite. El *trade-off* asumido es una ligera pérdida de exhaustividad en las respuestas puramente comerciales o de negocio (donde el modelo Flash demostró mayor iniciativa y detalle instructivo), un riesgo aceptable dado que el objetivo principal del chat es la resolución de dudas operativas del día a día del empleado.

## ¿Qué pasaría si duplicáramos el tráfico?

Duplicar el tráfico actual colapsaría de inmediato la aplicación bajo la arquitectura de API actual, tal y como han revelado los errores generalizados de código 429 (`RESOURCE_EXHAUSTED`) sufridos en los casos `p9` y `p10` al procesar de forma masiva las llamadas del benchmark. Al duplicar el volumen de empleados concurrentes, el sistema superará con creces el límite de peticiones por minuto (RPM). Para mitigar este riesgo técnico en producción, es obligatorio realizar el salto a un plan de pago corporativo (*Pay-as-you-go*) con cuotas garantizadas, además de implementar en el orquestador una cola de mensajes con políticas de **Exponential Backoff** y reintentos automáticos para controlar los picos de peticiones de los lunes por la mañana.

## Riesgo o condición

El despliegue en el entorno de producción queda estrictamente condicionado a la **implementación de un middleware de control de concurrencia y Rate Limiting** para subsanar la vulnerabilidad de cuota descubierta en este benchmark. Asimismo, se debe auditar el bloque de memoria conversacional para corregir la inercia de ambos modelos al emplear el saludo *"Bienvenida de nuevo"* en perfiles que se enfrentan a su primera jornada laboral, garantizando una experiencia de usuario totalmente coherente desde el primer clic.