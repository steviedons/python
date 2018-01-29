"""Car and ElectricCar class"""

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # default value of an attribute
        self.odometer_reading = 70

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print out a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value"""
        self.odometer_reading = mileage

# Class inheritance - the call inherits all the attributes and methods of the first class
# super() function links the child object to its parent

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # electric car only attribute
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
