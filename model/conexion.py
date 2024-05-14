# from flask_app import app
from flask_mysqldb import MySQL

class Conexion:
    def __init__(self,app):        
        # Configuración de la conexión a la base de datos
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'jersson'
        app.config['MYSQL_PASSWORD'] = 'jersson'
        app.config['MYSQL_DB'] = 'stock'
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Para obtener los resultados como diccionarios
        # Inicialización de la extensión MySQL
        self.mysql = MySQL(app)
        
    def consultaSinRetordo(self, sql):
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute(sql)
            self.mysql.connection.commit()
            return True
        except Exception as e:
            return False
    
    def consultaConRetordo(self, sql):
        cursor = self.mysql.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def consultaArray(self, sql):
        cursor = self.mysql.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result