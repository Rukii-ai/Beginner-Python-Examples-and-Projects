"""You can import as many classes as you need into a program file."""

from electric_car_module import Car, ElectricCar

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name()) 

my_leaf = ElectricCar('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name())

"""
You import multiple classes from a module by separating
each class with a comma ❶. Once you’ve imported the
necessary classes, you’re free to make as many instances of
each class as you need.
"""