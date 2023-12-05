Sebastian Rojas Osinaga
56814
# Analizador de Sentimiento de Frases
Este proyecto es un analizador de sentimiento de frases que utiliza FastAPI para crear una API que recibe frases en texto y devuelve información sobre el sentimiento inferido y la confianza asociada a esta inferencia.

## Descripción del Programa
El analizador de sentimiento de frases funciona de la siguiente manera: al proporcionar una frase en texto, el programa devuelve dos resultados clave:

1. **Etiqueta de Sentimiento**: Describe el sentimiento de la frase. Puede ser:

Muy Negativo
Negativo
Neutral
Positivo
Muy Positivo
2. **Puntaje de Confianza**: Indica qué tan seguro está el modelo con la etiqueta proporcionada. Este puntaje muestra la fiabilidad de la inferencia realizada por el modelo.

## Funciones de la API
### GET /status
Descripción: Verifica el estado del servicio.
Respuesta: Información sobre el estado del servicio, los modelos utilizados y el autor del proyecto.
POST /sentiment-analysis
Descripción: Realiza el análisis de sentimiento de una frase.
Entrada: Frase en formato de texto.
Salida:
Etiqueta de sentimiento.
Puntaje de confianza.
Tiempo de procesamiento.
POST /text-analysis
Descripción: Realiza un análisis completo de la frase.
Entrada: Frase en formato de texto.
Salida:
Etiqueta de sentimiento.
Puntaje de confianza.
Análisis detallado del texto, incluyendo:
Etiquetado de partes de la oración.
Entidades nombradas.
Incrustaciones de palabras.
Tiempo de procesamiento.
GET /reports
Descripción: Obtiene un informe en formato CSV.
Salida: Descarga un informe detallado de todas las inferencias realizadas.
Modelos Utilizados
Análisis de Texto: Utiliza el modelo es_core_news_sm de la biblioteca SpaCy para el análisis de texto.
Análisis de Sentimientos: Utiliza el modelo karina-aquino/spanish-sentiment-model de la biblioteca Transformers para el análisis de sentimientos en frases en español.