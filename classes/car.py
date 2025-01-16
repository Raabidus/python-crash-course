# Working with Classes and Instances

class Car:
    """A simple attem to represent car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given values
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery:
    """testy"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this abttery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_batery(self, upgrade = 100):
        if self.battery_size != 100:
            self.battery_size = upgrade


class ElectricCar(Car):
    """Represent of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialiaze attributes of the parent class Car"""
        super().__init__(make, model, year)
        self.battery = Battery()

# my_new_car = Car('Audi', 'a4', 2019)
# print(my_new_car.get_descriptive())

# # my_new_car.odometer_reading = 23
# my_new_car.update_odometer(7)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


