"""
Servicio para gestionar operaciones CRUD de usuarios.
"""
from database.db import DatabaseApi 
from models.usuario import Usuario 

class UsuarioService:
    """Servicio de lógica de negocio para usuarios."""
    def __init__(self):
        self.db = DatabaseApi()

    def listar(self):
        """Retorna todos los usuarios."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_usuario"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas

    def crear(self, usuario: Usuario):
        """Crea un nuevo usuario."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            INSERT INTO HM_usuario
                (nombre, apellido, correo, password_hash, rol, telefono)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.password_hash,
            usuario.rol,
            usuario.telefono
        )
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def buscar_por_id(self, id_usuario):
        """Busca un usuario por ID."""
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "SELECT * FROM HM_usuario WHERE id_usuario = %s"
        cur.execute(sql, (int(id_usuario),))
        fila = cur.fetchone()
        conn.close()
        return fila

    def actualizar(self, usuario: Usuario):
        """Actualiza un usuario existente."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = '''
            UPDATE HM_usuario
            SET nombre = %s,
                apellido = %s,
                correo = %s,
                password_hash = %s,
                rol = %s,
                telefono = %s
            WHERE id_usuario = %s
        '''
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.password_hash,
            usuario.rol,
            usuario.telefono,
            usuario.id_usuario
        )
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def eliminar(self, id_usuario):
        """Elimina un usuario por ID."""
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = "DELETE FROM HM_usuario WHERE id_usuario = %s"
        cur.execute(sql, (int(id_usuario),))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
