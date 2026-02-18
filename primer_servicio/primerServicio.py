from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/mensaje',methods=['GET'])

def mensaje():
    return jsonify('Bienvenidos programacion 3')
    
if __name__ == '__main__':
    app.run(debug=True)
