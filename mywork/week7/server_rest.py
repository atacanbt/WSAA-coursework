# very basic server REST API using Flask
# run this server and test it with curl or Postman

from flask import Flask, jsonify, request
from car_dao import CarDAO

app = Flask(__name__)

# Create a single instance of CarDAO to be used across all routes
car_dao = CarDAO()

@app.route('/')
def index():
    return 'Welcome to the Car API'

# Get all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(car_dao.get_cars())  # Use instance

# Get a car by id
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    return jsonify(car_dao.get_car(car_id))  # Use instance

# Create a new car
@app.route('/cars', methods=['POST'])
def add_car():
    # Read the JSON data from the client
    jsonstring = request.json
    # Required fields
    required_fields = {'brand', 'model', 'year', 'price'}
    # Check if all required fields exist
    if not jsonstring or not required_fields.issubset(jsonstring):
        return jsonify({"error": "Missing required fields"}), 400  # Return HTTP 400 Bad Request

    # Create car dictionary
    car = {
        'brand': jsonstring['brand'],
        'model': jsonstring['model'],
        'year': jsonstring['year'],
        'price': jsonstring['price']
    }

    new_car = car_dao.add_car(car)  # Use instance
    return jsonify(new_car), 201  # Return the created car with HTTP 201 status

# Update a car
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = request.get_json()
    updated_car = car_dao.update_car(car_id, car)  # Use instance
    return jsonify(updated_car)

# Delete a car
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    result = car_dao.delete_car(car_id)  # Use instance
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)