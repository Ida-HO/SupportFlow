"""
Servicio para gestionar técnicos a través de la API REST.
"""
import requests 
from CrudSistemaTickets.models.tecnico import Tecnico 

API_URL = "http://127.0.0.1:5000/tecnicos"

class TecnicoService:
    """Clase para interactuar con la API REST de técnicos."""
    def listar(self):
        """Obtiene la lista de técnicos desde la API."""
        response = requests.get(API_URL)
        return response.json()

    def crear(self, tecnico: Tecnico):
        """Crea un nuevo técnico a través de la API."""
        data = {
            "id_tecnico":tecnico.id_tecnico,
            "nombre":tecnico.nombre,
            "especialidad":tecnico.especialidad,
            "fecha_ingreso":tecnico.fecha_ingreso
        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 200

    def buscar_por_id(self, id_tecnico):
        """Busca un técnico por su ID a través de la API."""
        response = requests.get(f"{API_URL}/{id_tecnico}")
        if response.status_code == 200:
            return response.json()
        return None

    def actualizar(self, tecnico: Tecnico):
        """Actualiza un técnico existente a través de la API."""
        data = {
            "id_tecnico":tecnico.id_tecnico,
            "nombre":tecnico.nombre,
            "especialidad":tecnico.especialidad,
            "fecha_ingreso":tecnico.fecha_ingreso
        }
        response = requests.put(f"{API_URL}/{tecnico.id_tecnico}", json=data)
        return response.status_code == 200

    def eliminar(self, id_tecnico):
        """Elimina un técnico por su ID a través de la API."""
        response = requests.delete(f"{API_URL}/{id_tecnico}")
        return response.status_code == 200
