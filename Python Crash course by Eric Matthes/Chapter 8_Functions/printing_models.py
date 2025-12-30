"""
When you pass a list to a function, the function can modify
the list. Any changes made to the list inside the function’s
body are permanent, allowing you to work efficiently even
when you’re dealing with large amounts of data.
"""

# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design.title()}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed: ")
for model in completed_models:
    print(model)


"""
We can reorganize this code by writing two functions,
each of which does one specific job. Most of the code won’t
change; we’re just structuring it more carefully. The first
function will handle printing the designs, and the second will
summarize the prints that have been made
"""

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

def print_model(designs, models):
    """Accepts a list of unprinted model names and prints them"""
    while designs:
        model = designs.pop()
        print(f"Currently printing: {model.title()}")
        models.append(model)


def display_finished_models(models):
    """Display all completed models neatly"""
    print("\nThe following models were printed: ")
    for model in models:
        print(model.title())


print_model(unprinted_designs, completed_models)
display_finished_models(completed_models)

"""
A function is a reusable block of code that performs a specific task.
It can take inputs (arguments), process them, and optionally return a result.
Some functions modify mutable data in place, while others return new data.

This program is easier to extend and maintain than the
version without functions. If we need to print more designs
later on, we can simply call print_models() again. If we
realize the printing code needs to be modified, we can
change the code once, and our changes will take place
everywhere the function is called. This technique is more
efficient than having to update code separately in several
places in the program.

This example also demonstrates the idea that every
function should have one specific job. The first function
prints each design, and the second displays the completed
models. This is more beneficial than using one function to
do both jobs. If you’re writing a function and notice the
function is doing too many different tasks, try to split the
code into two functions. Remember that you can always call
a function from another function, which can be helpful when
splitting a complex task into a series of steps.
"""
