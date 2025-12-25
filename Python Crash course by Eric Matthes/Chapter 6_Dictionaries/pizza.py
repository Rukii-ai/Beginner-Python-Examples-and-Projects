# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

"""
When you need to break up a long line
in a print() call, choose an appropriate point at which to
break the line being printed, and end the line with a
quotation mark. Indent the next line, add an opening
quotation mark, and continue the string. Python will
automatically combine all of the strings it finds inside the
parentheses.
"""

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


