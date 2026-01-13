"""
Think of a class as a set of instructions for how to make an
instance. The Dog class is a set of instructions that tells
Python how to make individual instances representing
specific dogs
"""

class Dog: #Dog is the class
    """A simple attempt to model a dog."""
    
    """__init__ is a method and self, name and age are parameters
    When a class method is called on an instance of that class, 
    the particular instance itself is automatically passed as the first 
    argument to that method. The particular instance passes as an
    argument is passed into the parameter with name self"""
    
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
        """
        name and age are attributes. They take the values of name and age from
        #the parameter where the arguments are passed in during instance cretion
        the self. before them makes the variable (in this case attributes) 
        available to all methods in the class
        """
        

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


"""
Think of a class as a set of instructions for how to make an
instance. The Dog class is a set of instructions that tells
Python how to make individual instances representing
specific dogs.
"""

my_dog = Dog('Willie', 6)
"""
When Python
reads this line, it calls the __init__() method in Dog with the
arguments 'Willie' and 6.

The __init__() method creates an
instance representing this particular dog and sets the name
and age attributes using the values we provided. Python
then returns an instance representing this dog. We assign
that instance to the variable my_dog. 

The naming convention
is helpful here; we can usually assume that a capitalized
name like Dog refers to a class, and a lowercase name like
my_dog refers to a single instance created from a class.

Dot notation is used often in Python. This syntax
demonstrates how Python finds an attribute’s value. Here,
Python looks at the instance my_dog and then finds the
attribute name associated with my_dog. This is the same
attribute referred to as self.name in the class Dog. We use the
same approach to work with the attribute age
"""



"""
To access the attributes of an instance, you use dot
notation. 
"""
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")