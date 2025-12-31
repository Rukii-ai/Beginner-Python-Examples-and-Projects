"""
Because a function definition can have multiple parameters,
a function call may need multiple arguments. You can pass
arguments to your functions in a number of ways. You can
use positional arguments, which need to be in the same
order the parameters were written; keyword arguments,
where each argument consists of a variable name and a
value; and lists and dictionaries of values.

When you call a function, Python must match each
argument in the function call with a parameter in the
function definition. The simplest way to do this is based on
the order of the arguments provided. Values matched up
this way are called positional arguments.

You can call a function as many times as needed.
Calling a function multiple times is a very efficient way to
work. The code describing a pet is written once in the
function. Then, anytime you want to describe a new pet, you
call the function with the new pet’s information. Even if the
code for describing a pet were to expand to 10 lines, you
could still describe a new pet in just one line by calling the
function again
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')