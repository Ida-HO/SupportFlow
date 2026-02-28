"""
Servicio para gestionar tickets a través de la API REST.
"""
import requests 
from CrudSistemaTickets.models.ticket import Ticket 

API_URL = "http://127.0.0.1:5000/tickets"

class TicketService:
    """Clase para interactuar con la API REST de tickets."""
    def listar(self):
        """Obtiene la lista de tickets desde la API."""
        response = requests.get(API_URL)
        return response.json()

    def crear(self, ticket: Ticket):
        """Crea un nuevo ticket a través de la API."""
        data = {
            "id_ticket":ticket.id_ticket,
            "id_creador":ticket.id_creador,
            "id_tecnico":ticket.id_tecnico,
            "titulo":ticket.titulo,
            "descripcion":ticket.descripcion,
            "estado":ticket.estado,
            "fecha_creacion":ticket.fecha_creacion

        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 200

    def buscar_por_id(self, id_ticket):
        """Busca un ticket por su ID a través de la API."""
        response = requests.get(f"{API_URL}/{id_ticket}")
        if response.status_code == 200:
            return response.json()
        return None

    def actualizar(self, ticket: Ticket):
        """Actualiza un ticket existente a través de la API."""
        data = {
            "id_ticket":ticket.id_tecnico,
            "id_creador":ticket.id_creador,
            "id_tecnico":ticket.id_tecnico,
            "titulo":ticket.titulo,
            "descripcion":ticket.descripcion,
            "estado":ticket.estado,
            "fecha_creacion":ticket.fecha_creacion

        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 200

    def eliminar(self, id_ticket):
        """Elimina un ticket por su ID a través de la API."""
        response = requests.delete(f"{API_URL}/{id_ticket}")
        return response.status_code == 200
