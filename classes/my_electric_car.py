from car import ElectricCar

my_tesla = ElectricCar('tesla', 'models s', 2020)

print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()