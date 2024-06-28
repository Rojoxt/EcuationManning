from flask import Flask, request, jsonify

app = Flask(__name__)

def manning_equation(n, A, R, S):
    return (1 / n) * A * (R ** (2/3)) * (S ** (1/2))

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    n = data.get('n')
    A = data.get('A')
    R = data.get('R')
    S = data.get('S')
    Q = manning_equation(n, A, R, S)
    return jsonify({'Q': Q})

if __name__ == '__main__':
    app.run(debug=True)