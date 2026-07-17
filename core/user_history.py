from common.config import DIA_ONBOARDING
class UserHistory:
    def __init__(self, user_profile: dict, messages: list[dict] = None, dia_onboarding: int = DIA_ONBOARDING):
        '''
        Constructor

        user_profile: Sigue la estructura de los diccionarios del fichero empleados_demo
        messages: Lista de diccionarios. Los diccionarios siguen la siguiente estructura:
            {"role": "user"|"assistant", "text": "texto del mensaje"}

        '''
        self.user_profile = user_profile
        self.messages = messages if messages is not None else []
        self.turno = 0
        self.dia_onboarding = dia_onboarding

    def append_user_message(self, texto: str) -> None:
        """Añade mensaje del usuario al historial."""
        self.messages.append({"role": "user", "text": texto.strip()})

    def append_assistant_message(self, texto: str) -> None:
        """Añade respuesta del asistente al historial."""
        self.messages.append({"role": "assistant", "text": texto.strip()})
        self.turno += 1
    
    def ultimos_n(self, n: int) -> list[dict]:
        """Devuelve los últimos n mensajes."""
        return self.messages[-n:] if n > 0 else []

