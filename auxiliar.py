from google import genai
from llm.gemini.gemini_auth import configurar_gemini_api_key


configurar_gemini_api_key()
# Inicializa el cliente (recuerda tener tu GEMINI_API_KEY en el entorno)
client = genai.Client()

print("Modelos activos en tu cuenta:")

for m in client.models.list():
    # Filtramos solo los que sirven para chatear o generar texto
    if "generateContent" in m.supported_actions:
        # Limpiamos el prefijo 'models/' para que te quede el ID directo
        print(f"{m.name.replace('models/', '')}")