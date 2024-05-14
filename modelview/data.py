from model.consultas import Consulta

class Data:
    def __init__(self,conexion):
        self.consulta = Consulta(conexion)

    def categorias(self):
        data = self.consulta.categorias()
        return data