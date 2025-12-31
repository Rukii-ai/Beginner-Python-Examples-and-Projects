"""
Sometimes you won’t know ahead of time how many
arguments a function needs to accept. Fortunately, Python
allows a function to collect an arbitrary number of
arguments from the calling statement.
"""

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

"""
The asterisk in the parameter name *toppings tells Python
to make a tuple called toppings, containing all the values this
function receives. The print() call in the function body
produces output showing that Python can handle a function
call with one value and a call with three values. It treats the
different calls similarly. Note that Python packs the
arguments into a tuple, even if the function receives only
one value.

This syntax works no matter how many arguments the
function receives.
"""

