
from ControlGrua import *
from flask import Flask, request
app = Flask(__name__)


@app.route('/carroGrua', methods=['POST'])
def carro():
    print("CARRO GRUA")
    print(request.json)
    d = request.json['direccion']
    cg.moverCarroGrua(d)
    return {'response': 'moviendo carro grua'}

@app.route('/ganchoGrua', methods=['POST'])
def gancho():
    print("GANCHO GRUA")
    print(request.json)
    d = request.json['direccion']
    cg.moverGanchoGrua(d)
    return {'response': 'moviendo gancho grua'}


@app.route('/plumaGrua', methods=['POST'])
def pluma():
    print("PLUMA GRUA")
    print(request.json)
    d = request.json['direccion']
    cg.moverPlumaGrua(d)
    return {'response': 'moviendo pluma grua'}

if __name__ == '__main__':
    cg = ControlGrua()
    app.run(debug=True, port=8071, host='0.0.0.0')

