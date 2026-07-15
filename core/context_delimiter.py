from common.config import CUERPO_DIA_ONBOARDING, TAGS_DIA_ONBOARDING
from model.data_model import DataModel

def seleccionar_faqs(data_model: DataModel, empl: str, consulta: str, max_entradas: int, dia_onboarding: int) -> list[dict]:
    q = (consulta or "").lower()
    puntuaciones: list[tuple[int, dict]] = []
    empleado = data_model.empleados.getEmpleado(empl)

    for entry in data_model.getFaqs():
        score = 0
        for tag in entry.get("tags", []):
            if tag.lower() in q:
                score += 3
            if tag.lower() in empleado.get("departamento", "").lower():
                score += 1
            for dia_tag in TAGS_DIA_ONBOARDING.get(dia_onboarding, []):
                if dia_tag.lower() in tag.lower():
                    score += 2
        if score > 0:
            puntuaciones.append((score, entry))

    puntuaciones.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in puntuaciones[:max_entradas]]

def seleccionar_docs(faqs: list[dict], empl: str, data_model: DataModel, consulta: str, max_entradas: int, dia_onboarding: int) -> list[dict]:
    q = (consulta or "").lower()
    puntuaciones: list[tuple[int, dict]] = []
    empleado = data_model.empleados.getEmpleado(empl)

    for entry in data_model.getDocs():
        score = 0
        if match_docs_faqs(entry["id"], faqs):
            score +=90
        for tag in entry.get("tags", []):
            if tag.lower() in q:
                score += 4
            if tag.lower() in empleado.get("departamento", "").lower():
                score += 1
            for dia_tag in TAGS_DIA_ONBOARDING.get(dia_onboarding, []):
                if dia_tag.lower() in tag.lower():
                    score += 2
            # RMO: Esto solo lo hago en docs y no en faqs porque los docs son generalistas y los faqs son mas especificos. 
            for dia_cuerpo in CUERPO_DIA_ONBOARDING.get(dia_onboarding, []):
                if dia_cuerpo.lower() in entry.get("cuerpo", "").lower():
                    score += 2
        if score > 0:
            puntuaciones.append((score, entry))

    puntuaciones.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in puntuaciones[:max_entradas]]

def match_docs_faqs(id: str, faqs: list[dict]) -> bool:
    for i in faqs:
        if i.get("doc_id") and i["doc_id"].lower() == id.lower():
            return True
    return False