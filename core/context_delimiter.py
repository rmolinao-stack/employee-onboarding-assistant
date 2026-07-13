from model.data_model import DataModel

def seleccionar_faqs(data_model: DataModel, empl: str, consulta: str, max_entradas: int = 2) -> list[dict]:
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
        if score > 0:
            puntuaciones.append((score, entry))

    puntuaciones.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in puntuaciones[:max_entradas]]

def seleccionar_docs(faqs: list[dict], empl: str, data_model: DataModel, consulta: str, max_entradas: int = 4) -> list[dict]:
    q = (consulta or "").lower()
    puntuaciones: list[tuple[int, dict]] = []
    empleado = data_model.empleados.getEmpleado(empl)

    for entry in data_model.getDocs():
        score = 0
        if match_docs_faqs(entry["id"], faqs):
            score +=90
        for tag in entry.get("tags", []):
            if tag.lower() in q:
                score += 2
            if tag.lower() in empleado.get("departamento", "").lower():
                score += 1
        if entry.get("departamento", "").lower() in q:
            score += 1
        if score > 0:
            puntuaciones.append((score, entry))

    puntuaciones.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in puntuaciones[:max_entradas]]

def match_docs_faqs(id: str, faqs: list[dict]) -> bool:
    for i in faqs:
        if id == i["doc_id"]:
            return True
    return False