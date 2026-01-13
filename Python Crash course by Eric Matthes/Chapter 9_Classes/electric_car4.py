"""
When modeling something from the real world in code, you
may find that you’re adding more and more detail to a class.

You’ll find that you have a growing list of attributes and
methods and that your files are becoming lengthy. In these
situations, you might recognize that part of one class can be
written as a separate class.

You can break your large class
into smaller classes that work together; this approach is
called composition.
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


# Classes can serve as attributes for other classes
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Intialize the battery size attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
 


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        #In the line above "battery" is the attribute of the class ElectricCar
        # "Battery" is an instance of the class Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

"""
This line

my_leaf.battery.describe_battery()

tells Python to look at the instance my_leaf, find
its battery attribute, and call the method describe_battery()
that’s associated with the Battery instance assigned to the
attribute.
"""
