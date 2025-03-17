import mysql.connector
from config import keys as cfg


class CarDAO:
    host = cfg["host"]
    user = cfg["user"]
    password = cfg["root"]
    database = cfg["database"]

    connection = ""
    cursor = ""

    def __init__(self):
        self.cars = []  # In-memory list to store cars
        self.next_id = 1  # Auto-incrementing ID

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
        cursor = self.get_cursor()
        sql = "SELECT * FROM cars"
        cursor.execute(sql)
        result = cursor.fetchall()
        car_list = []
        for car in result:
            car_list.append(self.convert_to_dict(car))
        self.close_all()
        return car_list

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
        values = (car["brand"], car["model"], car["year"], car["price"])
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
        values = (updated_car["brand"], updated_car["model"], updated_car["year"], updated_car["price"], id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        return updated_car

    # Delete a car by ID
    def delete_car(self, id):
        cursor = self.get_cursor()
        sql = "DELETE FROM cars WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        return True

    def convert_to_dict(self, result_line):
        car_keys = ["id", "brand", "model", "year", "price"]
        current_key = 0
        car = {}
        for value in result_line:
            car[car_keys[current_key]] = value
            current_key += 1
        return car

carDao = CarDAO()