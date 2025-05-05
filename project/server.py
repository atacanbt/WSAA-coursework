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

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Car API'

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, jsonify, request, abort
# from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# cors = CORS(app) # allow CORS for all domains on all routes.
# app.config['CORS_HEADERS'] = 'Content-Type'

# from carDAO import CarDAO

# app = Flask(__name__, static_url_path='', static_folder='.')

# # Create a single instance of CarDAO to be used across all routes
# car_dao = CarDAO()

# @app.route('/')
# def index():
#     return 'Welcome to the Car API'

# # Get all cars
# @app.route('/cars', methods=['GET'])
# def get_cars():
#     return jsonify(car_dao.get_cars())  # Use instance

# # Get a car by id
# @app.route('/cars/<int:car_id>', methods=['GET'])
# def get_car(car_id):
#     return jsonify(car_dao.get_car(car_id))  # Use instance

# # Create a new car
# @app.route('/cars', methods=['POST'])
# def add_car():
#     # Read the JSON data from the client
#     jsonstring = request.json
#     # Required fields
#     required_fields = {'brand', 'model', 'year', 'price'}
#     # Check if all required fields exist
#     if not jsonstring or not required_fields.issubset(jsonstring):
#         return jsonify({"error": "Missing required fields"}), 400  # Return HTTP 400 Bad Request

#     # Create car dictionary
#     car = {
#         'brand': jsonstring['brand'],
#         'model': jsonstring['model'],
#         'year': jsonstring['year'],
#         'price': jsonstring['price']
#     }

#     new_car = car_dao.add_car(car)  # Use instance
#     return jsonify(new_car), 201  # Return the created car with HTTP 201 status

# # Update a car
# @app.route('/cars/<int:car_id>', methods=['PUT'])
# def update_car(car_id):
#     car = request.get_json()
#     updated_car = car_dao.update_car(car_id, car)  # Use instance
#     return jsonify(updated_car)

# # Delete a car
# @app.route('/cars/<int:car_id>', methods=['DELETE'])
# def delete_car(car_id):
#     result = car_dao.delete_car(car_id)  # Use instance
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)