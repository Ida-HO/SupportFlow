"""
Modelo de entidad TicketHistorial.
"""
class TicketHistorial:
    """Clase que representa historial de cambios de un ticket."""
    def __init__(self, id_historial=None, id_ticket=None,
                 estado_anterior=None, estado_nuevo="", fecha_cambio=None):
        self.id_historial = id_historial
        self.id_ticket = id_ticket
        self.estado_anterior = estado_anterior
        self.estado_nuevo = estado_nuevo
        self.fecha_cambio = fecha_cambio
