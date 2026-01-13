"""
Sometimes you’ll want to increment an attribute’s value by
a certain amount, rather than set an entirely new value. 
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


my_new_car = Car("subaru", "outback", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

"""
You can use methods like this to control how users of
your program update values such as an odometer
reading, but anyone with access to the program can
set the odometer reading to any value by accessing
the attribute directly. Effective security takes extreme
attention to detail in addition to basic checks like
those shown here.
"""