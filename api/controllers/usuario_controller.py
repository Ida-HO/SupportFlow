"""
Controlador para gestionar operaciones CRUD de ususarios.
"""
from flask import Blueprint, request, jsonify 
from services.usuario_service import UsuarioService 
from models.usuario import Usuario 

usuario_api = Blueprint("usuario_api", __name__)
service = UsuarioService()

@usuario_api.get("/usuarios")
def listar_usuarios():
    """Retorna la lista de todos los usuarios."""
    return jsonify(service.listar())

@usuario_api.post("/usuarios")
def crear_usuario():
    """Crea un nuevo usuario."""
    data = request.json
    usuario = Usuario(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        password_hash=data["password_hash"],
        rol=data.get("rol", "usuario"),
        telefono=data.get("telefono")
    )
    ok = service.crear(usuario)
    if ok:
        return jsonify({"msg": "Usuario creado con éxito."}), 201
    return jsonify({"msg": "Error al crear usuario."}), 400

@usuario_api.get("/usuarios/<int:id_usuario>")
def obtener_usuario(id_usuario):
    """Obtiene un usuario por su ID."""
    fila = service.buscar_por_id(id_usuario)
    if fila:
        return jsonify(fila)
    return jsonify({"msg": "Usuario no encontrado."}), 404

@usuario_api.put("/usuarios/<int:id_usuario>")
def actualizar_usuario(id_usuario):
    """Actualiza un usuario existente."""
    data = request.json
    usuario = Usuario(
        id_usuario=id_usuario,
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        password_hash=data["password_hash"],
        rol=data.get("rol", "usuario"),
        telefono=data.get("telefono")
    )
    ok = service.actualizar(usuario)
    if ok:
        return jsonify({"msg": "Usuario actualizado con éxito."})
    return jsonify({"msg": "Error al actualizar usuario."}), 400

@usuario_api.delete("/usuarios/<int:id_usuario>")
def eliminar_usuario(id_usuario):
    """Elimina un usuario por su ID."""
    ok = service.eliminar(id_usuario)
    if ok:
        return jsonify({"msg": "Usuario eliminado con éxito."})
    return jsonify({"msg": "Error al eliminar usuario."}), 400
