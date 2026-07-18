"""Generación de informes a partir de los resultados del benchmark.

Exporta las filas de resultados a un CSV con timestamp y produce un
informe Markdown con latencia media, tokens de salida y errores por modelo.
Los ficheros se guardan en la carpeta output/.
"""

import csv
from collections import defaultdict
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

from common.config import MODELS_BENCHMARK, OUTPUT_DIR, TEMPERATURE, LLM_PROVEEDOR
from common.utils import _stamp
from model.dataclasses.benchmark_dataclasses import FilaBenchmark

def _medias_por_modelo(filas: list[FilaBenchmark]) -> dict[str, dict[str, float]]:
    ok = [f for f in filas if not f.error]
    lat: dict[str, list[int]] = defaultdict(list)
    out_tok: dict[str, list[int]] = defaultdict(list)

    for f in ok:
        lat[f.modelo].append(f.elapsed_ms)
        if f.output_tokens is not None:
            out_tok[f.modelo].append(f.output_tokens)

    resumen: dict[str, dict[str, float]] = {}
    for modelo in MODELS_BENCHMARK:
        resumen[modelo] = {
            "runs_ok": float(len(lat.get(modelo, []))),
            "elapsed_ms_media": mean(lat[modelo]) if lat.get(modelo) else 0.0,
            "output_tokens_media": mean(out_tok[modelo]) if out_tok.get(modelo) else 0.0,
        }
    return resumen


def generar_reporte_md(filas: list[FilaBenchmark], csv_path: Path) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"report_{_stamp()}.md"
    medias = _medias_por_modelo(filas)
    errores = [f for f in filas if f.error]

    lineas = [
        "# Informe de benchmark — evaluador de modelos",
        "",
        f"- Generado: {datetime.now(timezone.utc).isoformat()}",
        f"- Temperatura: {TEMPERATURE}",
        f"- Proveedor: {LLM_PROVEEDOR}"
        f"- Modelos: {', '.join(MODELS_BENCHMARK)}",
        f"- CSV: `{csv_path.name}`",
        "",
        "## Latencia media (ms)",
        "",
        "| Modelo | Runs OK | ms media | out tokens media |",
        "|--------|---------|----------|------------------|",
    ]

    for modelo in MODELS_BENCHMARK:
        m = medias[modelo]
        lineas.append(
            f"| {modelo} | {int(m['runs_ok'])} | {m['elapsed_ms_media']:.0f} | "
            f"{m['output_tokens_media']:.1f} |"
        )

    lineas.extend(["", "## Errores", ""])
    if errores:
        for e in errores:
            lineas.append(f"- `{e.pregunta_id}` × `{e.modelo}`: {e.error}")
    else:
        lineas.append("Ninguno.")

    lineas.extend(
        [
            "",
            "## Siguiente paso",
            "",
            "Revisa respuestas en el CSV y asigna calidad 1–5 en una muestra.",
            "Documenta la decisión de modelo para cada caso de uso.",
            "",
        ]
    )

    path.write_text("\n".join(lineas), encoding="utf-8")
    return path
