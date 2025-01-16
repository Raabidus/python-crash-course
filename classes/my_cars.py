from car import Car
from eledtric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2001)
print(my_beetle.get_descriptive())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive())