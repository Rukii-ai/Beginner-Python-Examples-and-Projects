"""
You can get unexpected results if you mix up the order of
the arguments in a function call when using positional
arguments.

If you get funny results like this, check to make sure the
order of the arguments in your function call matches the
order of the parameters in the function’s definition.
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')  # Incorrect order