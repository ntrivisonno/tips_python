'''
Example for decorator/methods
@autor: ntrivisonno

The most popular methods are:
- instance methods
- @classmethod
- @staticmethod
- @properties
- @abstractmethod
- dunder methods
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @property
    def description(self):
        return f"Vehicle: {self.__class__.__name__}"

    @classmethod
    def count_vehicles(cls):
        return cls._total_vehicles

    @staticmethod
    def vehicle_info():
        return "This is a Vehicle class."

class Car(Vehicle):
    _total_vehicles = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._check_validity()
        Car._total_vehicles += 1

    def _check_validity(self):
        if not self.make or not self.model or not self.year:
            raise ValueError("Invalid Car details")

    def start_engine(self):
        print(f"The engine of {self.make} {self.model} ({self.year}) is now running.")

    @property
    def age(self):
        current_year = 2024
        return current_year - self.year

    @age.setter
    def age(self, value):
        print("Cannot set age directly. Use the year attribute.")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.make == other.make and
                    self.model == other.model and
                    self.year == other.year)
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.year < other.year
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Car):
            return f"Combined: {self.make} {self.model} ({self.year}) and {other.make} {other.model} ({other.year})"
        return NotImplemented

# Ejemplo de uso

# Usar métodos de clase y estáticos
print(Car.count_vehicles())  # Output: 0
print(Car.vehicle_info())  # Output: This is a Vehicle class.

# Crear instancias de Car
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

# Usar métodos de instancia
car1.start_engine()  # Output: The engine of Toyota Camry (2020) is now running.
print(car1.age)  # Output: 4 (si el año actual es 2024)

# Usar propiedades
print(car1.description)  # Output: Vehicle: Car

# Usar métodos especiales
print(car1)  # Output: Toyota Camry (2020)
print(repr(car1))  # Output: Car(make='Toyota', model='Camry', year=2020)
print(car1 == car2)  # Output: False
print(car1 < car2)  # Output: False (porque 2020 no es menor que 2018)
print(car1 + car2)  # Output: Combined: Toyota Camry (2020) and Honda Civic (2018)

# Verificar el número total de vehículos
print(Car.count_vehicles())  # Output: 2
