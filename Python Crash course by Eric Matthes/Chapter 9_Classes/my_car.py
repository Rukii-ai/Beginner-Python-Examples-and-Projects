from car_module import Car

my_new_car = Car('audi', 'a4', 2024) 
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

"""
Importing classes is an effective way to program. Picture
how long this program file would be if the entire Car class
were included. When you instead move the class to a
module and import the module, you still get all the same
functionality, but you keep your main program file clean and
easy to read.

You also store most of the logic in separate
files; once your classes work as you want them to, you can
leave those files alone and focus on the higher-level logic of
your main program.

You can store as many classes as you need in a single
module, although each class in a module should be related
somehow.
"""