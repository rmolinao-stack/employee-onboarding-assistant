from dataclasses import dataclass

@dataclass
class FilaBenchmark:
    timestamp: str
    pregunta_id: str
    modelo: str
    elapsed_ms: int
    prompt_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    respuesta: str
    error: str | None = None

@dataclass
class MetricasLlamada:
    elapsed_ms: int | None
    prompt_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None