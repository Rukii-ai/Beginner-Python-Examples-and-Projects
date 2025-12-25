cars = cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


"""At the heart of every if statement is an expression that can
be evaluated as True or False and is called a conditional test.
Python uses the values True and False to decide whether the
code in an if statement should be executed. If a conditional
test evaluates to True, Python executes the code following
the if statement. If the test evaluates to False, Python
ignores the code following the if statement"""

""" This equality operator returns True if
the values on the left and right side of the operator match,
and False if they don’t match."""

"""Testing for equality is case sensitive in Python."""