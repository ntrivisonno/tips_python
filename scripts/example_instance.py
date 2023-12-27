# example of instance in a class

class Car:
    
    # Variable that computes the number of cars created
    instances_created = 0
    all_cars = []

    def  __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.instances_created += 1
        Car.all_cars.append(self)

    @classmethod
    def print_all_instances(cls):
        for car in cls.all_cars: 
            print(f"Auto: {car.brand} Modelo: {car.model}")
    
auto1 = Car('Peugeot', '308')
auto2 = Car('Renault', 'Alaskan')


print('Se fabricaron {} autos'.format(Car.instances_created))
Car.print_all_instances()

print('#--------------------------------------------')
print('\n FIN, OK!')
