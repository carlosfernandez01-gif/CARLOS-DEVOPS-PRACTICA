import uuid

class Usuario:
    """Clase base para cualquier usuario del sistema.

    Atributos:
        id: Identificador único (uuid4).
        nombre: Nombre completo del usuario.
        email: Correo electrónico de contacto.
    """
    def __init__(self, nombre: str, email: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email

    def is_admin(self) -> bool:
        """Indica si el usuario tiene rol administrador."""
        return False

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} ({self.email})"


class Cliente(Usuario):
    """Usuario cliente con dirección postal para envíos."""
    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)
        self.direccion = direccion

    def __str__(self) -> str:
        return (f"[{self.id}] Cliente: {self.nombre} "
                f"({self.email}), Dirección: {self.direccion}")


class Administrador(Usuario):
    """Usuario con privilegios de administración."""
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[{self.id}] Administrador: {self.nombre} ({self.email})"