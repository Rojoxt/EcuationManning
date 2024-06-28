from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

def manning_equation(n, A, R, S):
    return (1 / n) * A * (R ** (2/3)) * (S ** (1/2))

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
    else:
        data = request.json
        n = data.get('n')
        A = data.get('A')
        R = data.get('R')
        S = data.get('S')
        Q = manning_equation(n, A, R, S)
        response = jsonify({'Q': Q})

    response.headers.add('Access-Control-Allow-Origin', 'https://codepen.io')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

@app.route('/', methods=['GET'])
def index():
    return "La aplicación está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
