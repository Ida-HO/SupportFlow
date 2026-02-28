"""
Modelo de datos para los usuarios del sistema.
"""
class Usuario:
    """Clase que representa un usuario del sistema."""
    def __init__(self, id_usuario=None, nombre="", apellido="", correo="", password_hash="", rol="usuario", telefono=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password_hash = password_hash
        self.rol = rol
        self.telefono = telefono
