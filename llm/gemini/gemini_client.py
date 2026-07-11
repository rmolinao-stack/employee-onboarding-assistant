from common.config import TEMPERATURE, MODEL
from google import genai
from google.genai import types


_client_instance: genai.Client | None = None

def _client() -> genai.Client:
    global _client_instance
    if _client_instance is None:
        _client_instance = genai.Client()
    return _client_instance

def llamar_gemini(
    prompt: str,
    *,
    temperature: float = TEMPERATURE,
) -> str:
    response = _client().models.generate_content(
    model=MODEL,
    contents=prompt,
    config=types.GenerateContentConfig(temperature=temperature),
    )
    return (response.text or "").strip()