"""
Controlador para gestionar operaciones CRUD de tickets.
"""
from flask import Blueprint, request, jsonify
from services.ticket_service import TicketService
from models.ticket import Ticket

ticket_api = Blueprint("ticket_api", __name__)
service = TicketService()

@ticket_api.get("/tickets")
def listar_tickets():
    """Retorna la lista de todos los tickets."""
    return jsonify(service.listar())

@ticket_api.post("/tickets")
def crear_ticket():
    """Crea un nuevo ticket."""
    data = request.json
    ticket = Ticket(
        id_creador=data["id_creador"],
        id_tecnico=data.get("id_tecnico"),
        titulo=data["titulo"],
        descripcion=data["descripcion"],
        estado=data.get("estado", "pendiente")
    )
    ok = service.crear(ticket)
    if ok:
        return jsonify({"msg": "Ticket creado con éxito."}), 201
    return jsonify({"msg": "Error al crear ticket."}), 400

@ticket_api.get("/tickets/<int:id_ticket>")
def obtener_ticket(id_ticket):
    """Obtiene un ticket por su ID."""
    fila = service.buscar_por_id(id_ticket)
    if fila:
        return jsonify(fila)
    return jsonify({"msg": "Ticket no encontrado."}), 404

@ticket_api.put("/tickets/<int:id_ticket>")
def actualizar_ticket(id_ticket):
    """Actualiza un ticket existente."""
    data = request.json
    ticket = Ticket(
        id_ticket=id_ticket,
        id_creador=data["id_creador"],
        id_tecnico=data.get("id_tecnico"),
        titulo=data["titulo"],
        descripcion=data["descripcion"],
        estado=data["estado"]
    )
    ok = service.actualizar(ticket)
    if ok:
        return jsonify({"msg": "Ticket actualizado con éxito."})
    return jsonify({"msg": "Error al actualizar ticket."}), 400

@ticket_api.delete("/tickets/<int:id_ticket>")
def eliminar_ticket(id_ticket):
    """Elimina un ticket por su ID."""
    ok = service.eliminar(id_ticket)
    if ok:
        return jsonify({"msg": "Ticket eliminado con éxito."})
    return jsonify({"msg": "Error al eliminar ticket."}), 400
