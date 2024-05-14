from model.conexion import Conexion

class Consulta:
    def __init__(self,conexion):
        self.con = conexion
        self.data = None

    def categorias(self):
        sql = "SELECT p.idcategoria, c.* FROM productos p JOIN categorias c ON p.idcategoria = c.idcategoria WHERE p.stock > 0 GROUP BY p.idcategoria, c.idcategoria, c.categoria HAVING COUNT(*) > 3;"
        result = self.con.consultaConRetordo(sql)
        return result
    def insertar(self, sql):
        sql = ""
        return self.con.consultaSinRetordo(sql)