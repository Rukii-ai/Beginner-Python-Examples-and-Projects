"""
You don’t always have to start from scratch when writing a
class. If the class you’re writing is a specialized version of
another class you wrote, you can use inheritance. When one
class inherits from another, it takes on the attributes and
methods of the first class. The original class is called the
parent class, and the new class is the child class. The child
class can inherit any or all of the attributes and methods of
its parent class, but it’s also free to define new attributes
and methods of its own.
"""

"""
When you’re writing a new class based on an existing class,
you’ll often want to call the __init__() method from the
parent class. This will initialize any attributes that were
defined in the parent __init__() method and make them
available in the child class.
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
        """Initialize attributes of parent class."""
        super().__init__(make, model, year)

my_leaf = ElectricCar("nissan", "leaf", "2024")
print(my_leaf.get_descriptive_name())



"""
We start with Car ❶. 

When you create a child class, the
parent class must be part of the current file and must
appear before the child class in the file. We then define the
child class, ElectricCar ❷. 

The name of the parent class must
be included in parentheses in the definition of a child class.
The __init__() method takes in the information required to
make a Car instance ❸.

The super() function ❹ is a special function that allows you
to call a method from the parent class. 

This line tells Python
to call the __init__() method from Car, which gives an
ElectricCar instance all the attributes defined in that
method. 

The name super comes from a convention of
calling the parent class a superclass and the child class a
subclass
"""