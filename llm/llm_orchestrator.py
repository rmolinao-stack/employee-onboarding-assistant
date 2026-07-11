from common.config import TEMPERATURE, LLM_PROVEEDOR
from llm.gemini.gemini_auth import configurar_gemini_api_key
from llm.gemini.gemini_client import llamar_gemini

def llamar_llm(prompt: str,
    *,
    temperature: float = TEMPERATURE,
):
    if LLM_PROVEEDOR == "GEMINI":
        configurar_gemini_api_key()
        return llamar_gemini(prompt=prompt, temperature=temperature)
    else:
        raise ValueError(f"Proveedor {LLM_PROVEEDOR} de LLM no está soportado.")