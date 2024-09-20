from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
        data = request.get_json()
        return jsonify({"received": data}), 201  # Retorna os dados recebidos e status 201 (Created)

if __name__ == '__main__':
    app.run(debug=True)