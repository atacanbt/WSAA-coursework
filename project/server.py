# This is a simple Flask application that provides a RESTful API for managing car data.
# It allows you to perform CRUD operations (Create, Read, Update, Delete) on car records.
# The application uses a CarDAO class to interact with the data layer, which is assumed to be implemented in a separate module.
# The API endpoints include:
# - GET /cars: Retrieve a list of all cars
# - GET /cars/<car_id>: Retrieve a specific car by its ID
# - POST /cars: Create a new car record
# - PUT /cars/<car_id>: Update an existing car record
# - DELETE /cars/<car_id>: Delete a car record by its ID
# Author: Atacan Buyuktalas

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import traceback
import logging
from carDAO import CarDAO

# Setup basic logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create a single instance of CarDAO to be used across all routes
car_dao = CarDAO()

@app.route('/')
@cross_origin()
def index():
    return app.send_static_file('carviewer.html')

# Get all cars
@app.route('/cars', methods=['GET'])
@cross_origin()
def get_cars():
    try:
        cars = car_dao.get_cars()
        return jsonify(cars)
    except Exception as e:
        print("Error in get_cars():", str(e))  # Log to PythonAnywhere logs
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Get a car by ID
@app.route('/cars/<int:car_id>', methods=['GET'])
@cross_origin()
def get_car(car_id):
    try:
        return jsonify(car_dao.get_car(car_id))
    except Exception as e:
        logging.error("Error fetching car with ID %d: %s", car_id, e)
        traceback.print_exc()
        return jsonify({"error": f"Failed to fetch car {car_id}", "details": str(e)}), 500

# Create a new car
@app.route('/cars', methods=['POST'])
@cross_origin()
def add_car():
    try:
        jsonstring = request.get_json()
        logging.debug("Received JSON: %s", jsonstring)

        required_fields = {'brand', 'model', 'year', 'price'}
        if not jsonstring or not required_fields.issubset(jsonstring):
            return jsonify({"error": "Missing required fields"}), 400

        car = {
            'brand': jsonstring['brand'],
            'model': jsonstring['model'],
            'year': jsonstring['year'],
            'price': jsonstring['price']
        }

        new_car = car_dao.add_car(car)
        return jsonify(new_car), 201
    except Exception as e:
        logging.error("Error adding car: %s", e)
        traceback.print_exc()
        return jsonify({"error": "Failed to add car", "details": str(e)}), 500

# Update a car
@app.route('/cars/<int:car_id>', methods=['PUT'])
@cross_origin()
def update_car(car_id):
    try:
        car = request.get_json()
        updated_car = car_dao.update_car(car_id, car)
        return jsonify(updated_car)
    except Exception as e:
        logging.error("Error updating car ID %d: %s", car_id, e)
        traceback.print_exc()
        return jsonify({"error": f"Failed to update car {car_id}", "details": str(e)}), 500

# Delete a car
@app.route('/cars/<int:car_id>', methods=['DELETE'])
@cross_origin()
def delete_car(car_id):
    try:
        result = car_dao.delete_car(car_id)
        return jsonify(result)
    except Exception as e:
        logging.error("Error deleting car ID %d: %s", car_id, e)
        traceback.print_exc()
        return jsonify({"error": f"Failed to delete car {car_id}", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)