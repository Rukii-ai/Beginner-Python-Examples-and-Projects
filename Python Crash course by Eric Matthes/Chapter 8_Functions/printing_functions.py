# Functions for printing_models.py
# Seperated and placed into a module

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