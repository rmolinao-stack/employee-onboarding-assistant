import time
from common.config import TEMPERATURE, MODEL
from google import genai
from google.genai import types
from model.dataclasses.benchmark_dataclasses import MetricasLlamada


_client_instance: genai.Client | None = None

def _client() -> genai.Client:
    global _client_instance
    if _client_instance is None:
        _client_instance = genai.Client()
    return _client_instance

def llamar_gemini(
    prompt: str,
    *,
    llm_model: str = MODEL,
    temperature: float = TEMPERATURE,
) -> tuple[str, MetricasLlamada]:
    started = time.time()
    response = _client().models.generate_content(
    model=llm_model,
    contents=prompt,
    config=types.GenerateContentConfig(temperature=temperature),
    )
    elapsed_ms = int((time.time() - started) * 1000)
    um = response.usage_metadata
    metricas = MetricasLlamada(
        elapsed_ms=elapsed_ms,
        prompt_tokens=getattr(um, "prompt_token_count", None),
        output_tokens=getattr(um, "candidates_token_count", None),
        total_tokens=getattr(um, "total_token_count", None),
    )
    return (response.text or "").strip(), metricas