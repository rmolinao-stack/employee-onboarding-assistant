import re


SUSPICIOUS_INJECTION_PATTERNS = [
    r"ignora(?:r)? (?:las )?(?:instrucciones|reglas|prioridades|indicaciones|todo)",
    r"olvida(?:r)? (?:que|lo)",
    r"ahora eres",
    r"revela(?:r)?",
    r"contrase(?:\u00f1|n)a",
    r"token",
    r"api key",
    r"secreto",
]

SENSITIVE_DATA_PATTERNS = [
    r"\b(salario|sueldo|bonus|comisi[oó]n|cobra|gana|paga|remuneraci[oó]n)\b",
]

OUT_OF_DOMAIN_PATTERNS = [
    r"\b(ejercicio|examen|curso externo|programa formativo|tarea de universidad|practica|práctica)\b",
]

POLICY_PATTERNS = [
    r"\b(pol[ií]tica|norma|regla|ley|plazo|vacaciones|ausencia)\b",
]

AMBIGUOUS_MEDICAL_PATTERNS = [
    r"\b(baja|m[eé]dica|operaci[oó]n|hospital|medicinas|enfermedad)\b",
]


def validar_mensaje_usuario(user_msg: str) -> tuple[bool, str]:
    mensaje = (user_msg or "").strip()

    if not mensaje:
        return False, "El mensaje está vacío."

    if len(mensaje) > 400:
        return False, "El mensaje es demasiado largo para un turno de onboarding."

    texto = mensaje.lower()

    if any(re.search(pattern, texto) for pattern in SUSPICIOUS_INJECTION_PATTERNS):
        return False, "Se detectó un intento de inyección de instrucciones."

    if any(re.search(pattern, texto) for pattern in SENSITIVE_DATA_PATTERNS):
        return False, "No puedo ayudar con datos sensibles o compensación."

    if any(re.search(pattern, texto) for pattern in OUT_OF_DOMAIN_PATTERNS):
        return False, "La solicitud está fuera del alcance del onboarding interno."

    if any(re.search(pattern, texto) for pattern in POLICY_PATTERNS) and any(
        palabra in texto for palabra in ["permitido", "prohibido", "obligatorio", "cuanto", "cuántos", "cuál", "qué"]
    ):
        return False, "No puedo confirmar políticas no documentadas."

    if any(re.search(pattern, texto) for pattern in AMBIGUOUS_MEDICAL_PATTERNS):
        return False, "La solicitud es ambigua entre salud y laboral; requiere derivación a RRHH o salud laboral."

    return True, ""


def construir_respuesta_segura(razon: str) -> str:
    return (
        "No puedo atender esta solicitud de forma segura. "
        "Solo puedo ayudar con preguntas documentadas sobre onboarding para empleados nuevos. "
        f"Motivo: {razon}"
    )
