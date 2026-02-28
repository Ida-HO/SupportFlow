"""
Modelo de datos para el técnico en el sistema de tickets.
"""
class Tecnico:
    """Clase que representa a un técnico en el sistema de tickets."""
    def __init__(self, id_tecnico=None, nombre="", especialidad="", fecha_ingreso=None):
        self.id_tecnico = id_tecnico
        self.nombre = nombre
        self.especialidad = especialidad
        self.fecha_ingreso = fecha_ingreso
