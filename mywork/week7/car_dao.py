


class CarDAO:
    def __init__(self):
        self.cars = []  # In-memory list to store cars
        self.next_id = 1  # Auto-incrementing ID

    # Get all cars
    def get_cars(self):
        return self.cars

    # Get a car by ID
    def get_car(self, car_id):
        for car in self.cars:
            if car["id"] == car_id:
                return car
        return None  # Return None if not found

    # Create a new car
    def add_car(self, car):
        car["id"] = self.next_id
        self.cars.append(car)
        self.next_id += 1
        return car

    # Update a car by ID
    def update_car(self, car_id, updated_car):
        for car in self.cars:
            if car["id"] == car_id:
                car.update(updated_car)  # Update existing car data
                return car
        return None  # Return None if not found

    # Delete a car by ID
    def delete_car(self, car_id):
        for i, car in enumerate(self.cars):
            if car["id"] == car_id:
                return self.cars.pop(i)  # Remove and return the deleted car
        return None  # Return None if not found