"""
Servicio para gestionar operaciones CRUD de tickets.
"""
from database.db import DatabaseApi 
from models.ticket import Ticket 

class TicketService:
    """Servicio de lógica de negocio para tickets."""
    def __init__(self):
        self.db = DatabaseApi()

    def listar(self):
        """Retorna todos los tickets."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_ticket"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas

    def crear(self, ticket: Ticket):
        """Crea un nuevo ticket."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            INSERT INTO HM_ticket
                (id_creador, id_tecnico, titulo, descripcion, estado)
            VALUES (%s, %s, %s, %s, %s)
        '''
        valores = (
            ticket.id_creador,
            ticket.id_tecnico,
            ticket.titulo,
            ticket.descripcion,
            ticket.estado
        )
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def buscar_por_id(self, id_ticket):
        """Busca un ticket por ID."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_ticket WHERE id_ticket = %s"
        cur.execute(sql, (int(id_ticket),))
        fila = cur.fetchone()
        conn.close()
        return fila

    def actualizar(self, ticket: Ticket):
        """Actualiza un ticket existente."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            UPDATE HM_ticket
            SET id_creador = %s,
                id_tecnico = %s,
                titulo = %s,
                descripcion = %s,
                estado = %s
            WHERE id_ticket = %s
        '''
        valores = (
            ticket.id_creador,
            ticket.id_tecnico,
            ticket.titulo,
            ticket.descripcion,
            ticket.estado,
            ticket.id_ticket
        )
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def eliminar(self, id_ticket):
        """Elimina un ticket por ID."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = "DELETE FROM HM_ticket WHERE id_ticket = %s"
        cur.execute(sql, (int(id_ticket),))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
