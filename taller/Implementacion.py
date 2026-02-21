from ListaEnlazada import ListaEnlazada
from Carro import Carro
from flask import Flask,request,jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)
lista_carros = ListaEnlazada()

@app.route('/agregarAlInicio', methods=['POST'])
@swag_from('agregarAlInicio.yml')
def agregarAlInicio():
    datos = request.get_json()
    identifier = datos.get('identifier')
    marca = datos.get('marca')
    precio = datos.get('precio')
    placa = datos.get('placa')
    nuevoCarro = Carro(identifier,marca,precio,placa)
    lista_carros.agregar_al_frente(nuevoCarro)
    return jsonify({'mensaje': 'Carro agregado correctamente'})

@app.route('/agregarAlFinal', methods=['POST'])
@swag_from('agregarAlFinal.yml')
def agregarAlFinal():
    datos = request.get_json()
    identifier = datos.get('identifier')
    marca = datos.get('marca')
    precio = datos.get('precio')
    placa = datos.get('placa')
    nuevoCarro = Carro(identifier,marca,precio,placa)
    lista_carros.agregar_al_final(nuevoCarro)
    return jsonify({'mensaje': 'Carro agregado correctamente'})    

@app.route('/listaEnlazada', methods=['GET'])
@swag_from('listaEnlazada.yml')
def mostrarListaEnlazada():
    return lista_carros.imprimir_lista_objetos()

@app.route('/buscarPorId', methods=['POST'])
@swag_from('buscarPorId.yml')
def buscarPorIdLista():
    datos = request.get_json()
    identifier = datos.get('identifier')
    return jsonify(lista_carros.buscarPorId(identifier).to_json())

@app.route('/eliminar', methods=['DELETE'])
@swag_from('eliminar.yml')
def eliminar():
    datos = request.get_json()
    identifier = datos.get('identifier')  
    lista_carros.eliminarPorId(identifier) 
    return lista_carros.imprimir_lista_objetos()

@app.route('/actualizar', methods=['PUT'])
@swag_from('actualizar.yml')
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
