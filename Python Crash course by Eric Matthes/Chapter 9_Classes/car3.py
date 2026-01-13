"""
You can change an attribute’s value in three ways: you can
change the value directly through an instance, set the value
through a method, or increment the value (add a certain
amount to it) through a method.
"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Intialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return n neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

"""
We use dot notation to access the car’s odometer_reading
attribute, and set its value directly. This line tells Python to
take the instance my_new_car, find the attribute
odometer_reading associated with it, and set the value of that
attribute to 23:

Sometimes you’ll want to access attributes directly like
this, but other times you’ll want to write a method that
updates the value for you.
"""