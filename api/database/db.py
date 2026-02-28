"""
Módulo de conexión a base de datos MySQL.
"""
import mysql.connector 

class DatabaseApi:
    """Clase para gestionar la conexión a la base de datos."""
    def __init__(self):
        """Inicializa configuración de conexión."""
        self.config = {
            "host":"138.255.103.114",
            "port":3306,
            "user":"inacodec_poo_seccion_c2",
            "password":"AQm}ZzpW0ovqyaZJ",
            "database":"inacodec_dataPracticaApis"
        }
    
    def conectar(self):
        """Establece conexión con la base de datos.
           Retorna objeto conexión o None si falla.
        """
        try:
            conn = mysql.connector.connect(**self.config)
            return conn        
        except mysql.connector.Error as err:
            print(f"Error de conexion: {err}")
            return None
