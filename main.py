from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # Esto permite solicitudes CORS desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        n = data.get('n')
        A = data.get('A')
        R = data.get('R')
        S = data.get('S')
        result = (1 / n) * A * (R ** (2/3)) * (S ** (1/2))
        return jsonify({'result': result}),200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    return "La aplicación está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
