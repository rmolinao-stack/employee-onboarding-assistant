import re
from common.config import MSG_LENGTH_LIMIT, SUSPICIOUS_INJECTION_PATTERNS, SENSITIVE_DATA_PATTERNS, OUT_OF_DOMAIN_PATTERNS, POLICY_PATTERNS, AMBIGUOUS_MEDICAL_PATTERNS

def validar_mensaje_usuario(user_msg: str) -> tuple[bool, str]:
    mensaje = (user_msg or "").strip()

    if not mensaje:
        return False, "El mensaje está vacío."

    if len(mensaje) > MSG_LENGTH_LIMIT:
        return False, "El mensaje es demasiado largo para un turno de onboarding."

    texto = mensaje.lower()

    if any(re.search(pattern, texto) for pattern in SUSPICIOUS_INJECTION_PATTERNS):
        return False, "El mensaje contiene palabras no permitidas."
    
    return True, ""

def construir_respuesta_segura(razon: str) -> str:
    return (
        "No puedo atender esta solicitud de forma segura. "
        "Solo puedo ayudar con preguntas documentadas sobre onboarding para empleados nuevos. "
        f"Motivo: {razon}"
    )
