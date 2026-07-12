import json
from pathlib import Path

def cargar_json(ruta: Path):
    with ruta.open(encoding="utf-8") as f:
        data = json.load(f)
    return data