from flask import Flask, render_template, request, jsonify
from modelview.data import Data
from model.conexion import Conexion

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
conexion = Conexion(app)


@app.route('/')
def index():
    datos = Data(conexion)
    resp = datos.categorias()
    print(resp)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
