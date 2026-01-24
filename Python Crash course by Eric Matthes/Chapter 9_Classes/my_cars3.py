from car_module import Car
from electric_car2_module import ElectricCar

my_mustang = Car('ford', 'mustang', 2024) 
print(my_mustang.get_descriptive_name()) 

my_leaf = ElectricCar('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name())


"""
As you saw in Chapter 8, aliases can be quite helpful when
using modules to organize your projects’ code. You can use
aliases when importing classes as well.

As an example, consider a program where you want to
make a bunch of electric cars. It might get tedious to type
(and read) ElectricCar over and over again. You can give
ElectricCar an alias in the import statement:

from electric_car import ElectricCar as EC

Now you can use this alias whenever you want to make an
electric car:

my_leaf = EC('nissan', 'leaf', 2024)

You can also give a module an alias. Here’s how to import
the entire electric_car module using an alias:

import electric_car as ec

Now you can use this module alias with the full class
name:

my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)

As you can see, Python gives you many options for how to
structure code in a large project. It’s important to know all
these possibilities so you can determine the best ways to
organize your projects as well as understand other people’s
projects.

When you’re starting out, keep your code structure
simple. Try doing everything in one file and moving your
classes to separate modules once everything is working. 

If you like how modules and files interact, try storing your
classes in modules when you start a project. Find an
approach that lets you write code that works, and go from
there
"""