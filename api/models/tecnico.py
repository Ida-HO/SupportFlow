"""
Modelo de entidad Técnico.
"""
class Tecnico:
    """Clase que representa un técnico del sistema."""
    def __init__(self, id_tecnico=None, nombre="", especialidad="", fecha_ingreso=None): # Inicializador del modelo Técnico
        self.id_tecnico = id_tecnico
        self.nombre = nombre
        self.especialidad = especialidad
        self.fecha_ingreso = fecha_ingreso
