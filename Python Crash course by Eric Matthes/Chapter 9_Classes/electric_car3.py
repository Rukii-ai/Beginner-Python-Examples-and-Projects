"""
You can override any method from the parent class that
doesn’t fit what you’re trying to model with the child class.

To do this, you define a method in the child class with the
same name as the method you want to override in the
parent class. Python will disregard the parent class method
and only pay attention to the method you define in the child
class.
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

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


"""
Now if someone tries to call fill_gas_tank() with an electric
car, Python will ignore the method fill_gas_tank() in Car and
run this code instead. When you use inheritance, you can
make your child classes retain what you need and override
anything you don’t need from the parent class.
"""