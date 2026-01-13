"""
You can model almost anything using classes. Let’s start by
writing a simple class, Dog, that represents a dog—not one
dog in particular, but any dog. What do we know about most
pet dogs? Well, they all have a name and an age. We also
know that most dogs sit and roll over. Those two pieces of
information (name and age) and those two behaviors (sit
and roll over) will go in our Dog class because they’re
common to most dogs. This class will tell Python how to
make an object representing a dog. After our class is
written, we’ll use it to make individual instances, each of
which represents one specific dog.
"""

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

"""
We first define a class called Dog. By
convention, capitalized names refer to classes in Python.
There are no parentheses in the class definition because
we’re creating this class from scratch. We then write a
docstring describing what this class does
"""