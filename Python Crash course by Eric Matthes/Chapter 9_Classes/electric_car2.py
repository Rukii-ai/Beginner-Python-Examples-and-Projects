"""
Once you have a child class that inherits from a parent
class, you can add any new attributes and methods
necessary to differentiate the child class from the parent
class
"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Intialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer (self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if someone tries to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        "Add the given amount to odometer reading"
        if miles > 0:
            self.odometer_reading += miles
        elif miles < 0:
            print("You can't roll back an odometer")
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


"""
There’s no limit to how much you can specialize the
ElectricCar class.

You can add as many attributes and
methods as you need to model an electric car to whatever
degree of accuracy you need. 

An attribute or method that
could belong to any car, rather than one that’s specific to an
electric car, should be added to the Car class instead of the
ElectricCar class. 

Then anyone who uses the Car class will
have that functionality available as well, and the ElectricCar
class will only contain code for the information and behavior
specific to electric vehicles
"""