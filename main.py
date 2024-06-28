from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/calculate": {"origins": "https://cdpn.io"}})

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'OPTIONS request successful'})
        response.headers.add('Access-Control-Allow-Origin', 'https://cdpn.io')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    try:
        data = request.json
        n = float(data.get('n'))  # Convertir a float si es necesario
        A = float(data.get('A'))
        R = float(data.get('R'))
        S = float(data.get('S'))
        result = (1 / n) * A * (R ** (2/3)) * (S ** (1/2))
        return jsonify({'Q': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    return "La aplicación está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
