"""
Controlador para gestionar el historial de tickets.
"""
from flask import Blueprint, request, jsonify 
from services.ticket_historial_service import TicketHistorialService 
from models.ticket_historial import TicketHistorial 

ticket_historial_api = Blueprint("ticket_historial_api", __name__, url_prefix="/ticket_historial")
service = TicketHistorialService()

@ticket_historial_api.get("/")
def listar_historial():
    """Lista todos los registros de historial."""
    return jsonify(service.listar())


@ticket_historial_api.get("/ticket/<int:id_ticket>")
def listar_historial_por_ticket(id_ticket):
    """Lista el historial de un ticket específico."""
    return jsonify(service.listar_por_ticket(id_ticket))

@ticket_historial_api.post("/ticket_historial")
def crear_historial():
    """Crea un nuevo registro de historial."""
    data = request.json
    hist = TicketHistorial(
        id_ticket=data["id_ticket"],
        estado_anterior=data.get("estado_anterior"),
        estado_nuevo=data["estado_nuevo"]
    )
    ok = service.crear(hist)
    if ok:
        return jsonify({"msg": "Historial creado con éxito."}), 201
    return jsonify({"msg": "Error al crear historial."}), 400

@ticket_historial_api.get("/ticket_historial/<int:id_historial>")
def obtener_historial(id_historial):
    """Obtiene un registro de historial por ID."""
    fila = service.buscar_por_id(id_historial)
    if fila:
        return jsonify(fila)
    return jsonify({"msg": "Registro de historial no encontrado."}), 404

@ticket_historial_api.delete("/ticket_historial/<int:id_historial>")
def eliminar_historial(id_historial):
    """Elimina un registro de historial por ID."""
    ok = service.eliminar(id_historial)
    if ok:
        return jsonify({"msg": "Historial eliminado con éxito."})
    return jsonify({"msg": "Error al eliminar historial."}), 400
