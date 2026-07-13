class UserHistory:
    def __init__(self, user_profile: dict, messages: list[dict] = []):
        '''
        Constructor

        user_profile: Sigue la estructura de los diccionarios del fichero empleados_demo
        messages: Lista de diccionarios. Los diccionarios siguen la siguiente estructura:
            {"role": "user"|"assistant", "text": "texto del mensaje"}

        '''
        self.user_profile = user_profile
        self.messages = messages
        self.turnos = 0

    def append_user_message(self, texto: str) -> None:
        """Añade mensaje del usuario al historial."""
        self.messages.append({"role": "user", "text": texto.strip()})

    def append_assistant_message(self, texto: str) -> None:
        """Añade respuesta del asistente al historial."""
        self.messages.append({"role": "assistant", "text": texto.strip()})
        # self.turnos += 1
    
    def ultimos_n(self, n: int) -> list[dict]:
        """Devuelve los últimos n mensajes."""
        print("=" * 120)
        print(f"HAY QUE ARREGAR ***ultimos_n*** PORQUE NO DEVUELVE LOS ULTIMOS TURNOS SINO LOS ULTIMOS MENSAJES!!!! VER EL CODIGO ORIGINAL!!!!!")
        print("=" * 120)
        return self.messages[-n:] if n > 0 else []

