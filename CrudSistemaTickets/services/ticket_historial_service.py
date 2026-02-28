"""
Servicio para gestionar el historial de tickets a través de la API REST.
"""
import requests 
from CrudSistemaTickets.models.ticket_historial import TicketHistorial 

API_URL = "http://127.0.0.1:5000/ticket_historial"

class TicketHistorialService:
    """Clase para interactuar con la API REST de historial de tickets."""
    def listar(self):
        """Obtiene la lista de historial de tickets desde la API."""
        response = requests.get(API_URL)
        return response.json()

    def listar_por_ticket(self, id_ticket):
        """Obtiene el historial de un ticket específico desde la API."""
        url = f"{API_URL}/ticket/{id_ticket}"
        response = requests.get(url)
        return response.json()

    def crear(self, hist: TicketHistorial):
        """Crea un nuevo historial de ticket a través de la API."""
        data = {
            "id_ticket": hist.id_ticket,
            "estado_anterior": hist.estado_anterior,
            "estado_nuevo": hist.estado_nuevo
        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 201

    def buscar_por_id(self, id_historial):
        """Busca un historial de ticket por su ID a través de la API."""
        url = f"{API_URL}/{id_historial}"
        response = requests.get(url)
        return response.json()

    def eliminar(self, id_historial):
        """Elimina un historial de ticket por su ID a través de la API."""
        url = f"{API_URL}/{id_historial}"
        response = requests.delete(url)
        return response.status_code == 200
