from ListaEnlazada import ListaEnlazada
from Carro import Carro
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
lista_carros = ListaEnlazada()

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return jsonify({'mensaje': 'Listas Enlazadas'})

@app.route('/agregarAlInicio', methods=['POST'])
def agregarAlInicio():
    datos = request.get_json()
    marca = datos.get('marca')
    precio = datos.get('precio')
    placa = datos.get('placa')
    nuevoCarro = Carro(marca,precio,placa)
    lista_carros.agregar_al_frente(nuevoCarro)
    return jsonify({'mensaje': 'Carro agregado correctamente'})

@app.route('/listaEnlazada', methods=['GET'])
def mostrarListaEnlazada():
    return lista_carros.imprimir_lista_objetos()

if __name__ == '__main__':
    app.run(debug=True)
