from flask import Flask, request, jsonify
from flask_cors import CORS
import math  # Importar el módulo math


app = Flask(__name__)
CORS(app)  # Esto permite solicitudes CORS desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/calcular', methods=['POST'])
def calcular_bernoulli():
    try:
        data = request.json
        P = data.get('P')
        p = data.get('p')
        v = data.get('v')
        g = data.get('g')
        h = data.get('h')

        resultado = P + (0.5 * p * math.pow(v, 2)) + (p * g * h)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    return "La aplicación BernoulliAPI está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)