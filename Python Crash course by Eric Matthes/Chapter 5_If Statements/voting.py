"""
The simplest kind of if statement has one test and one action:

if conditional_test: 
    do something

You can put any conditional test in the first line and just
about any action in the indented block following the test. If
the conditional test evaluates to True, Python executes the
code following the if statement. If the test evaluates to
False, Python ignores the code following the if statement.
"""

age = 19
age = 17
if age >= 18:
    print("You are old enough to vote!")
    
    """
    You can have as many lines of code as you want in the
    block following the if statement.
    """
    
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

"""
Often, you’ll want to take one action when a conditional test
passes and a different action in all other cases. Python’s if
else syntax makes this possible. An if-else block is similar to
a simple if statement, but the else statement allows you to
define an action or set of actions that are executed when
the conditional test fails.

The if-else structure works well in
situations in which you want Python to always execute one
of two possible actions. In a simple if-else chain like this,
one of the two actions will always be executed
"""
