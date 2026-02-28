"""
Servicio para gestionar usuarios a través de la API REST.
"""
import requests 
from CrudSistemaTickets.models.usuario import Usuario 

API_URL = "http://127.0.0.1:5000/usuarios"

class UsuarioService:
    """Clase para interactuar con la API REST de usuarios."""
    def listar(self):
        """Obtiene la lista de usuarios desde la API."""
        response = requests.get(API_URL)
        return response.json()

    def crear(self, usuario: Usuario):
        """Crea un nuevo usuario a través de la API."""
        data = {
            "id_usuario":usuario.id_usuario,
            "nombre":usuario.nombre,
            "apellido":usuario.apellido,
            "correo":usuario.correo,
            "password_hash":usuario.password_hash,
            "rol":usuario.rol,
            "telefono":usuario.telefono
        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 200

    def buscar_por_id(self, id_usuario):
        """Busca un usuario por su ID a través de la API."""
        response = requests.get(f"{API_URL}/{id_usuario}")
        if response.status_code == 200:
            return response.json()
        return None

    def actualizar(self, usuario: Usuario):
        """Actualiza un usuario existente a través de la API."""
        data = {
            "id_usuario":usuario.id_usuario,
            "nombre":usuario.nombre,
            "apellido":usuario.apellido,
            "correo":usuario.correo,
            "password_hash":usuario.password_hash,
            "rol":usuario.rol,
            "telefono":usuario.telefono
        }
        response = requests.put(f"{API_URL}/{usuario.id_usuario}", json=data)
        return response.status_code == 200

    def eliminar(self, id_usuario):
        """Elimina un usuario por su ID a través de la API."""
        response = requests.delete(f"{API_URL}/{id_usuario}")
        return response.status_code == 200
