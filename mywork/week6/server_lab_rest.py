# very basic server REST API using Flask
# run this server and test it with curl or Postman

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, This is a car database!</h1>"

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify()

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    return jsonify({'car_id': car_id})

@app.route('/cars', methods=['POST'])
def add_car():
    car = request.get_json()
    return jsonify(car), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = request.get_json()
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)