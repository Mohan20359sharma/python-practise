'''
6. Create a class Vehicle with attributes brand, model, and year. Write a method vehicle_info() to display the vehicle details. Extend it into a Car class with an additional attribute mileage.
'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.brand} {self.model} {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year,mileage):
        super().__init__(brand, model, year)
        self.mileage = mileage

    def car_info(self):
        return f"{self.vehicle_info()} with {self.mileage} miles."
    
car = Car("Toyota", "Camry", 2020, 15000)
print(car.car_info())