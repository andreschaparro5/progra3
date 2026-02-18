from flask import Flask,request,jsonify
from Vehiculo import ObjetoVehiculo
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

vehiculos = []

nuevoVehiculo = ObjetoVehiculo('2009', 'Mazda', 'Gris', 'LCS-203')

vehiculos.append(nuevoVehiculo.to_json())



@app.route('/listarVehiculos', methods=['GET'])

def obtenerVehiculos():
    return jsonify(vehiculos)

if __name__ == '__main__':
    app.run(debug=True)
