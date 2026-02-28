"""
Modelo de datos para los tickets de soporte.
"""
class Ticket:
    """Clase que representa un ticket de soporte."""
    def __init__(self, id_ticket=None, id_creador=None, id_tecnico=None,
                 titulo="", descripcion="", estado="pendiente", fecha_creacion=None):
        self.id_ticket = id_ticket
        self.id_creador = id_creador
        self.id_tecnico = id_tecnico
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_creacion = fecha_creacion
