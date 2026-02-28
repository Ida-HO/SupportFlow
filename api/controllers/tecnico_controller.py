"""
Controlador para gestionar operaciones CRUD de técnicos.
"""
from flask import Blueprint, request, jsonify
from services.tecnico_service import TecnicoService
from models.tecnico import Tecnico


tecnico_api = Blueprint("tecnico_api", __name__)
service = TecnicoService()

@tecnico_api.get("/tecnicos")
def listar_tecnicos():
    """Retorna la lista de todos los técnicos."""
    return jsonify(service.listar())

@tecnico_api.post("/tecnicos")
def crear_tecnico():
    """Crea un nuevo técnico."""
    data = request.json
    tecnico = Tecnico(
        nombre=data["nombre"],
        especialidad=data.get("especialidad", "")
    )
    ok = service.crear(tecnico)
    if ok:
        return jsonify({"msg": "Técnico creado con éxito."}), 201
    return jsonify({"msg": "Error al crear técnico."}), 400

@tecnico_api.get("/tecnicos/<int:id_tecnico>")
def obtener_tecnico(id_tecnico):
    """Obtiene un técnico por su ID."""
    fila = service.buscar_por_id(id_tecnico)
    if fila:
        return jsonify(fila)
    return jsonify({"msg": "Técnico no encontrado."}), 404

@tecnico_api.put("/tecnicos/<int:id_tecnico>")
def actualizar_tecnico(id_tecnico):
    """Actualiza los datos de un técnico existente."""
    data = request.json
    tecnico = Tecnico(
        id_tecnico=id_tecnico,
        nombre=data["nombre"],
        especialidad=data.get("especialidad", "")
    )
    ok = service.actualizar(tecnico)
    if ok:
        return jsonify({"msg": "Técnico actualizado con éxito."})
    return jsonify({"msg": "Error al actualizar técnico."}), 400

@tecnico_api.delete("/tecnicos/<int:id_tecnico>")
def eliminar_tecnico(id_tecnico):
    """Elimina un técnico por su ID."""
    ok = service.eliminar(id_tecnico)
    if ok:
        return jsonify({"msg": "Técnico eliminado con éxito."})
    return jsonify({"msg": "Error al eliminar técnico."}), 400
