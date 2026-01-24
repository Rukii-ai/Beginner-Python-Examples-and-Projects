"""
Sometimes you’ll want to spread out your classes over
several modules to keep any one file from growing too large
and avoid storing unrelated classes in the same module.

When you store your classes in several modules, you may
find that a class in one module depends on a class in
another module. When this happens, you can import the
required class into the first module"""



"""A set of classes that can be used to represent electric ca
rs.""" 

from car_module import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Intialize the battery size attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
 


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
