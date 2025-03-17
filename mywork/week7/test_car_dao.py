from car_dao import carDao


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "price": 5000
}
# Add a new car
car = carDao.add_car(car)
car_id = car["id"]
print("Added car with ID:", car_id)

# Find the car by ID
result = carDao.get_car(car_id)
print("Found car by ID:", car)
print(result)

# Update the car
new_car_values = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "price": 6000
}
updated_car = carDao.update_car(car_id, new_car_values)
print("Updated car with ID:", car_id)
print(updated_car)

# Get all cars
cars = carDao.get_cars()
for car in cars:
    print(car)

# Delete the car
# carDao.delete_car(car_id)
# print("Deleted car with ID:", car_id)
