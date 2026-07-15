import json
from pathlib import Path
from textwrap import indent

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