from model.conexion import Conexion

class Consulta:
    def __init__(self,conexion):
        self.con = conexion
        self.data = None
    def computadoras(self):
        sql = "select * from computadoras where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def componentes(self):
        sql = "select * from componentes where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def impresoras(self):
        sql = "select * from impresoras where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def portatiles(self):
        sql = "select * from portatiles where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def accesorios(self):
        sql = "select * from perifericos_accesorios where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def multimedia(self):
        sql = "select * from equipos_multimedia where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    def consumibles(self):
        sql = "select * from consumibles where stock > 0;"
        result = self.con.consultaConRetordo(sql)
        return result
    # DETALLES DEL PRODUCTO
    def detalles(self,id):
        sql = f"select * from productos where id = {id};"
        result = self.con.consultaArray(sql)
        return result