from ListaEnlazada import ListaEnlazada
from Carro import Carro
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
lista_carros = ListaEnlazada()

@app.route('/agregarAlInicio', methods=['POST'])
def agregarAlInicio():
    datos = request.get_json()
    identifier = datos.get('identifier')
    marca = datos.get('marca')
    precio = datos.get('precio')
    placa = datos.get('placa')
    nuevoCarro = Carro(identifier,marca,precio,placa)
    lista_carros.agregar_al_frente(nuevoCarro)
    return jsonify({'mensaje': 'Carro agregado correctamente'})

@app.route('/listaEnlazada', methods=['GET'])
def mostrarListaEnlazada():
    return lista_carros.imprimir_lista_objetos()

@app.route('/buscarPorId', methods=['POST'])
def buscarPorIdLista():
    datos = request.get_json()
    identifier = datos.get('identifier')
    return jsonify(lista_carros.buscarPorId(identifier).to_json())

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    datos = request.get_json()
    identifier = datos.get('identifier')  
    lista_carros.eliminarPorId(identifier) 
    return lista_carros.imprimir_lista_objetos()

@app.route('/actualizar', methods=['PUT'])
def actualizar():
    datos = request.get_json()
    identifier = datos.get('identifier')
    marca = datos.get('marca')
    precio = datos.get('precio')
    placa = datos.get('placa')
    nuevoCarro = Carro(identifier,marca,precio,placa)
    lista_carros.actualizar(identifier, nuevoCarro)
    return lista_carros.imprimir_lista_objetos()   

if __name__ == '__main__':
    app.run(debug=True)
