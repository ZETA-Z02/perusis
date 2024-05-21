from flask import Flask, render_template, request, jsonify
from modelview.data import Data
from model.conexion import Conexion

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
# Se le pasa una instancia de la app a la clase conexion
# INICIALIZA LA CONEXION
conexion = Conexion(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    datos = request.json  # Obtener los datos JSON de la solicitud
    # Ahora puedes trabajar con los datos recibidos
    question = datos.get('content')
    # Se le da como parametro el objeto de la conexion, para pueda utilizar sus metodos
    datos = Data(conexion)
    resp = datos.categorias()
    print(resp)
    print(question)
    return jsonify({'resultado': resp})

@app.route('/email', methods=['POST'])
def email():
    datos = Data(conexion)
    data = request.get_json()
    email = data.get('content')
    id = data.get('id')
    resp = datos.detallesCorreo(email,id)
    return jsonify({'resultado': resp})

@app.route('/chatbot1', methods=['POST'])
def chatbot1():
    data = request.get_json()
    entrada = data.get('content')
    resp = master(entrada)
    return jsonify({'resultado': resp})


def master(entrada):
    datos = Data(conexion)
    opciones = ['1','2','3','4','5','6','7']
    if entrada not in opciones and entrada.isdigit() == False:
        resp = datos.categorias(entrada)
        return resp
    
    if entrada == '1': 
        resp = datos.computadoras()
        return resp
    elif entrada == '2': 
        resp = datos.componentes()
        return resp
    elif entrada == '3': 
        resp = datos.impresoras()
        return resp
    elif entrada == '4': 
        resp = datos.portatiles()
        return resp
    elif entrada == '5': 
        resp = datos.accesorios()
        return resp
    elif entrada == '6': 
        resp = datos.multimedia()
        return resp
    elif entrada == '7': 
        resp = datos.consumibles()
        return resp
    elif len(entrada) > 1: 
        resp = datos.detalles(entrada)
        return resp
    
if __name__ == '__main__':
    app.run(debug=True)
