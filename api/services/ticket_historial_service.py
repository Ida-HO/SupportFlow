"""
Servicio para gestionar operaciones CRUD de historial de tickets.
"""
from database.db import DatabaseApi 
from models.ticket_historial import TicketHistorial 

class TicketHistorialService:
    """Servicio de lógica de negocio para historial de tickets."""
    def __init__(self):
        self.db = DatabaseApi()

    def listar(self):
        """Retorna todos los registros de historial."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_ticket_historial"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas

    def listar_por_ticket(self, id_ticket):
        """Retorna historial asociado a un ticket específico."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_ticket_historial WHERE id_ticket = %s"
        cur.execute(sql, (int(id_ticket),))
        filas = cur.fetchall()
        conn.close()
        return filas

    def crear(self, hist: TicketHistorial):
        """Crea un nuevo registro de historial."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            INSERT INTO HM_ticket_historial
                (id_ticket, estado_anterior, estado_nuevo)
            VALUES (%s, %s, %s)
        '''
        valores = (
            hist.id_ticket,
            hist.estado_anterior,
            hist.estado_nuevo
        )
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def buscar_por_id(self, id_historial):
        """Busca un registro de historial por ID."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_ticket_historial WHERE id_historial = %s"
        cur.execute(sql, (int(id_historial),))
        fila = cur.fetchone()
        conn.close()
        return fila

    def eliminar(self, id_historial):
        """Elimina un registro de historial por ID."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = "DELETE FROM HM_ticket_historial WHERE id_historial = %s"
        cur.execute(sql, (int(id_historial),))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
