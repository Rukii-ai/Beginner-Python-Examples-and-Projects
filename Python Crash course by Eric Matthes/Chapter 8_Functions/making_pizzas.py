import pizza3

pizza3.make_pizza(16, "pepperoni")
pizza3.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

"""
When Python reads this file, the line import pizza3 tells
Python to open the file pizza3.py and copy all the functions
from it into this program. You don’t actually see code being
copied between files because Python copies the code
behind the scenes, just before the program runs. All you
need to know is that any function defined in pizza3.py will
now be available in making_pizzas.py

To call a function from an imported module, enter the
name of the module you imported, pizza3, followed by the
name of the function, make_pizza(), separated by a dot.
This code produces the same output as the original program
that didn’t import a module:

This first approach to importing, in which you simply write
import followed by the name of the module, makes every
function from the module available in your program. If you
use this kind of import statement to import an entire module
named module_name.py, each function in the module is
available through the following syntax:

module_name.function_name()

"""