from ListaEnlazada import ListaEnlazada
from EstudianteGestion import Estudiante
from flask import Flask,request,jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)
lista_estudiantes = ListaEnlazada()


@app.route('/mensaje',methods=['GET'])
@swag_from('mensaje.yml')
def mensaje():
    return jsonify({'mensaje': 'Listas Enlazadas'})

@app.route('/agregarAlInicio', methods=['POST'])
@swag_from('agregarAlInicio.yml')
def agregarAlInicio():
    datos = request.get_json()
    nombre = datos.get('nombre')
    edad = datos.get('edad')
    identificacion = datos.get('identificacion')
    nuevoEstudiante = Estudiante(nombre,edad,identificacion)
    lista_estudiantes.agregar_al_frente(nuevoEstudiante)
    return jsonify({'mensaje': 'Estudiante agregado correctamente'})

@app.route('/listaEnlazada', methods=['GET'])
@swag_from('mostrarListaEnlazada.yml')
def mostrarListaEnlazada():
    return lista_estudiantes.imprimir_lista_objetos()

if __name__ == '__main__':
    app.run(debug=True)
