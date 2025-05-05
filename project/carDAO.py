# File: carDAO.py
# This script defines a CarDAO class that interacts with a MySQL database to perform CRUD operations on car data.
# It includes methods to get all cars, get a car by ID, add a new car, update a car by ID, and delete a car by ID.
# Author: Atacan Buyuktalas

import mysql.connector
from dbconfig import mysql as cfg
# from config import keys as cfg

class CarDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        self.host = cfg["host"]
        self.user = cfg["user"]
        self.password = cfg["password"]
        self.database = cfg["database"]

    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def close_all(self):
        self.connection.close()
        self.cursor.close()

    # Get all cars
    def get_cars(self):
       try:
            cursor = self.get_cursor()
            sql = "SELECT * FROM cars"
            cursor.execute(sql)
            result = cursor.fetchall()
            car_list = []
            for car in result:
                if car: 
                    car_list.append(self.convert_to_dict(car))
        
            self.close_all()
            return car_list
       except Exception as e:
            print("Error in CarDAO.get_cars:", str(e))
            self.close_all()
            raise

    # Get a car by ID
    def get_car(self, id):
        cursor = self.get_cursor()
        sql = "SELECT * FROM cars WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.close_all()
        return self.convert_to_dict(result)

    # Create a new car
    def add_car(self, car):
        cursor = self.get_cursor()
        sql = "INSERT INTO cars (brand, model, year, price) VALUES (%s, %s, %s, %s)"
        values = (car.get("brand"), car.get("model"), car.get("year"), car.get("price"))
        cursor.execute(sql, values)

        self.connection.commit()
        new_id = cursor.lastrowid
        car["id"] = new_id
        self.close_all()
        return car

    # Update a car by ID
    def update_car(self, id, updated_car):
        cursor = self.get_cursor()
        sql = "UPDATE cars SET brand = %s, model = %s, year = %s, price = %s WHERE id = %s"
        print(f"Updating car {updated_car}")
        values = (updated_car.get("brand"), updated_car.get("model"), updated_car.get("year"), updated_car.get("price"), id)

        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        return updated_car

    # Delete a car by ID
    def delete_car(self, id):
        cursor = self.get_cursor()
        sql = "DELETE FROM cars WHERE id = %s"
        values = (id,)
        print(f"Deleting car with ID {id}")
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        print(f"Car with ID {id} deleted successfully")
        return True

    def convert_to_dict(self, result_line):
        car_keys = ["id", "brand", "model", "year", "price"]
        current_key = 0
        car = {}
        for value in result_line:
            car[car_keys[current_key]] = value
            current_key = current_key + 1
        return car

carDao = CarDAO()