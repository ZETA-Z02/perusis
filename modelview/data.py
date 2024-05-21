from model.consultas import Consulta
from modelview.correo import EmailMessage
class Data:
    def __init__(self,conexion):
        self.consulta = Consulta(conexion)
        self.email = EmailMessage("jersson.z032@gmail.com","fxws idjg pqjo hmjd")

    def categorias(self,nombre):
        if isinstance(nombre,str):
            nombre = nombre
        else:
            nombre = "usuario"
            
        categorias = f"""
                    <li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hola {nombre} tenemos los siguientes productos: <br>1.Computadoras<br>2.Componentes<br>3.impresoras<br>4.portatiles<br>5.accesorios<br>6.equipos multimedia<br>7.consumibles</p>
                    </li>"""
        return categorias
    def computadoras(self):
        datas = self.consulta.computadoras()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def componentes(self):
        datas = self.consulta.componentes()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def impresoras(self):
        datas = self.consulta.impresoras()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def portatiles(self):
        datas = self.consulta.portatiles()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def accesorios(self):
        datas = self.consulta.accesorios()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def multimedia(self):
        datas = self.consulta.multimedia()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    def consumibles(self):
        datas = self.consulta.consumibles()
        html =""
        for data in datas:
            html += f"{data['id']}. {data['categoria']} de {data['marca']} <br>"
        
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p>Hay estos productos con estas marcas:<br>{html} seleccione el numero del producto para mas detalles</p>
                    </li>"""
        return res
    
    def detalles(self,id):
        data = self.consulta.detalles(id)
        res = f"""<li class="chat incoming">
                        <span class="material-symbols-outlined">smart_toy</span>
                        <p id="{data['id']}">{data['id']}:{data['modelo']}<br><br>Ingrese su correo y se le enviara la informacion detallada
                        <input type="email" id="email" placeholder="su Email por favor"/><span id="send-email" class="material-symbols-rounded">send</span></p>
                    </li>"""
        return res
    def detallesCorreo(self,email,id):
        data = self.consulta.detalles(id)
        destino = email
        asunto = "Detalles del producto que usted consulto"
        message = f"el modelo del producto es: {data['modelo']}, de la marca: {data['idmarca']}, con un precio de: {data['precio']} y se vende por: {data['tipoventa']}"
        result = self.email.sendMessage(destino,asunto,message)
        return result
        