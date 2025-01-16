from car import Car


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