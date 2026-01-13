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

my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()



"""
As you begin to model more complicated things like electric
cars, you’ll wrestle with interesting questions.

Is the range
of an electric car a property of the battery or of the car? If
we’re only describing one car, it’s probably fine to maintain
the association of the method get_range() with the Battery
class. But if we’re describing a manufacturer’s entire line of
cars, we probably want to move get_range() to the
ElectricCar class. 

The get_range() method would still check
the battery size before determining the range, but it would
report a range specific to the kind of car it’s associated with.
Alternatively, we could maintain the association of the
get_range() method with the battery but pass it a parameter
such as car_model. The get_range() method would then report
a range based on the battery size and car model.


This brings you to an interesting point in your growth as a
programmer. When you wrestle with questions like these,
you’re thinking at a higher logical level rather than a syntax
focused level. 

You’re thinking not about Python, but about
how to represent the real world in code. When you reach
this point, you’ll realize there are often no right or wrong
approaches to modeling real-world situations. 

Some
approaches are more efficient than others, but it takes
practice to find the most efficient representations. If your
code is working as you want it to, you’re doing well! Don’t
be discouraged if you find you’re ripping apart your classes
and rewriting them several times using different
approaches.

In the quest to write accurate, efficient code,
everyone goes through this process
"""
