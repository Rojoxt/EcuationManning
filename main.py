from flask import Flask, request, jsonify
from flask_cors import CORS
import math  # Importar el módulo math

app = Flask(__name__)
CORS(app)  # Esto permite solicitudes CORS desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/calcula', methods=['POST'])
def calcular_bernoulli():
    try:
        data = request.json
        n = float(data.get('n'))  # Convertir a float si es necesario
        A = float(data.get('A'))
        R = float(data.get('R'))
        S = float(data.get('S'))
        result = (1/n) * A * math.pow(R, 2/3) * math.sqrt(S)
        return jsonify({'Q': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/', methods=['GET'])
def index():
    return "La aplicación  ecuacion de manning está corriendo correctamente"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
