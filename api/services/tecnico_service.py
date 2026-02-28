"""
Servicio para gestionar operaciones CRUD de técnicos.
"""
from database.db import DatabaseApi 
from models.tecnico import Tecnico 

class TecnicoService:
    """Servicio de lógica de negocio para técnicos."""
    def __init__(self):
        self.db = DatabaseApi()

    def listar(self):
        """Retorna lista de técnicos."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_tecnico"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas

    def crear(self, tecnico: Tecnico):
        """Crea un nuevo técnico."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            INSERT INTO HM_tecnico (nombre, especialidad)
            VALUES (%s, %s)
        '''
        valores = (tecnico.nombre, tecnico.especialidad)
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def buscar_por_id(self, id_tecnico):
        """Busca un técnico por ID."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_tecnico WHERE id_tecnico = %s"
        cur.execute(sql, (int(id_tecnico),))
        fila = cur.fetchone()
        conn.close()
        return fila

    def actualizar(self, tecnico: Tecnico):
        """Actualiza un técnico existente."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            UPDATE HM_tecnico
            SET nombre = %s,
                especialidad = %s
            WHERE id_tecnico = %s
        '''
        valores = (tecnico.nombre, tecnico.especialidad, tecnico.id_tecnico)
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def eliminar(self, id_tecnico):
        """Elimina un técnico por ID."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = "DELETE FROM HM_tecnico WHERE id_tecnico = %s"
        cur.execute(sql, (int(id_tecnico),))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
