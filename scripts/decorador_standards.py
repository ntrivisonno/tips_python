# example of standard decorators
from abc import ABC, abstractmethod

class Vehicle(ABC):
    total_vehicles = 0  # Variable de clase para todos los vehículos

    def __init__(self, brand, model, year, vehicle_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.vehicle_type = vehicle_type
        Vehicle.total_vehicles += 1  # Incrementa la cuenta total de vehículos

    @abstractmethod
    def display_info(self):
        pass  # Método abstracto que deberá implementarse en subclases

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles  # Método de clase para acceder al total de vehículos

    def __str__(self):
        return f'{self.year} {self.brand} {self.model} ({self.vehicle_type})'

class Car(Vehicle):
    cars_by_brand = {}  # Variable de clase para contar coches por marca

    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year, 'Car')  # Llama al constructor de la superclase
        self.fuel_type = fuel_type
        # Contabilizar el coche por su marca
        if brand in Car.cars_by_brand:
            Car.cars_by_brand[brand] += 1
        else:
            Car.cars_by_brand[brand] = 1

    @staticmethod
    def possible_brands():
        return ['Toyota', 'Ford', 'BMW', 'Mercedes', 'Tesla']

    @classmethod
    def get_cars_by_brand(cls):
        return cls.cars_by_brand  # Método de clase para acceder al total de coches por marca

    def display_info(self):
        return f'{self.year} {self.brand} {self.model}, Fuel: {self.fuel_type}'

    def __str__(self):
        return super().__str__() + f' ({self.fuel_type})'

class Motorcycle(Vehicle):
    motorcycles_by_brand = {}  # Variable de clase para contar motocicletas por marca

    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year, 'Motorcycle')  # Llama al constructor de la superclase
        self.engine_capacity = engine_capacity  # En cc (centímetros cúbicos)
        # Contabilizar la motocicleta por su marca
        if brand in Motorcycle.motorcycles_by_brand:
            Motorcycle.motorcycles_by_brand[brand] += 1
        else:
            Motorcycle.motorcycles_by_brand[brand] = 1

    @classmethod
    def get_motorcycles_by_brand(cls):
        return cls.motorcycles_by_brand  # Método de clase para acceder al total de motocicletas por marca

    def display_info(self):
        return f'{self.year} {self.brand} {self.model}, Engine Capacity: {self.engine_capacity}cc'

    def __str__(self):
        return super().__str__() + f' ({self.engine_capacity}cc)'

# Ejemplos de uso

car1 = Car('Toyota', 'Corolla', 2020, 'Petrol')
bike1 = Motorcycle('Honda', 'CB500F', 2021, 500)

print(car1.display_info())  # 2020 Toyota Corolla, Fuel: Petrol
print(bike1.display_info())  # 2021 Honda CB500F, Engine Capacity: 500cc

print(Car.get_total_vehicles())  # 2
print(Motorcycle.get_motorcycles_by_brand())  # {'Honda': 1}
