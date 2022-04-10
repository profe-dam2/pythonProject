
from ControlGrua import *
from flask import Flask, request
app = Flask(__name__)


@app.route('/carroGrua', methods=['POST'])
def carro():
    d = request.json['direccion']
    ControlGrua().moverCarroGrua(d)
    return {'response': 'moviendo carro grua'}

@app.route('/ganchoGrua', methods=['POST'])
def carro():
    d = request.json['direccion']
    ControlGrua().moverGanchoGrua(d)
    return {'response': 'moviendo carro grua'}

if __name__ == '__main__':
    ControlGrua()
    app.run(debug=True, port=8071, host='0.0.0.0')

