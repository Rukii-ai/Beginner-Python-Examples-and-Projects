"""
When writing a function, you can define a default value for
each parameter. If an argument for a parameter is provided
in the function call, Python uses the argument value. If not,
it uses the parameter’s default value. So when you define a
default value for a parameter, you can exclude the
corresponding argument you’d usually write in the function
call. Using default values can simplify your function calls
and clarify the ways your functions are typically used
"""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
describe_pet('spot')
describe_pet(pet_name='harry', animal_type='hamster')

"""
Note that the order of the parameters in the function
definition had to be changed. Because the default value
makes it unnecessary to specify a type of animal as an
argument, the only argument left in the function call is the
pet’s name. Python still interprets this as a positional
argument, so if the function is called with just a pet’s name,
that argument will match up with the first parameter listed
in the function’s definition. This is the reason the first
parameter needs to be pet_name

Because an explicit argument for animal_type is provided,
Python will ignore the parameter’s default value

When you use default values, any parameter with a
default value needs to be listed after all the
parameters that don’t have default values. This allows
Python to continue interpreting positional arguments
correctly.
"""

"""
Because positional arguments, keyword arguments, and
default values can all be used together, you’ll often have
several equivalent ways to call a function.

It doesn’t really matter which calling style you use. As
long as your function calls produce the output you want, just
use the style you find easiest to understand.
"""


"""
When you start to use functions, don’t be surprised if you
encounter errors about unmatched arguments. Unmatched
arguments occur when you provide fewer or more
arguments than a function needs to do its work.

Python is helpful in that it reads the function’s code for us
and tells us the names of the arguments we need to
provide. This is another motivation for giving your variables
and functions descriptive names. If you do, Python’s error
messages will be more useful to you and anyone else who
might use your code

Python is helpful in that it reads the function’s code for us
and tells us the names of the arguments we need to
provide. This is another motivation for giving your variables
and functions descriptive names. If you do, Python’s error
messages will be more useful to you and anyone else who
might use your code
"""