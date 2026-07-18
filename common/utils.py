import json
import csv
from pathlib import Path
from textwrap import indent
from datetime import datetime, timezone
from dataclasses import asdict
from statistics import mean

def cargar_json(ruta: Path):
    with ruta.open(encoding="utf-8") as f:
        data = json.load(f)
    return data

def imprimir_contexto_seleccionado(faqs: list[dict], docs: list[dict]) -> None:
    print("\nContexto seleccionado:")

    if faqs:
        print("  FAQs:")
        for faq in faqs:
            print(f"    - Pregunta: {faq.get('pregunta', '')}")
            print(indent(faq.get('respuesta_corta', ''), "      "))
    else:
        print("  FAQs: ninguna")

    if docs:
        print("  Docs:")
        for doc in docs:
            print(f"    - Título: {doc.get('titulo', '')}")
            print(indent(doc.get('cuerpo', ''), "      "))
    else:
        print("  Docs: ninguno")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def guardar_csv(filas: list, output_dir: str, prefix: str) -> Path:
    output_dir.mkdir(exist_ok=True)
    path = output_dir / f"{prefix}{_stamp()}.csv"
    if not filas:
        path.write_text("", encoding="utf-8")
        return path

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(filas[0]).keys()))
        writer.writeheader()
        for fila in filas:
            writer.writerow(asdict(fila))
    return path