import json
from pathlib import Path

def cargar_json(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("faq.json debe ser una lista de entradas")
    return data