def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()

"""
The first line uses the keyword def to inform Python that
you’re defining a function. This is the function definition,
which tells Python the name of the function and, if
applicable, what kind of information the function needs to
do its job. The parentheses hold that information. Finally, the
definition ends in a colon.

Any indented lines that follow def greet_user(): make up
the body of the function. The text on the second line is a
comment called a docstring, which describes what the
function does.

When Python generates documentation for
the functions in your programs, it looks for a string
immediately after the function's definition. These strings are
usually enclosed in triple quotes, which lets you write
multiple lines

When you want to use this function, you have to call it. A
function call tells Python to execute the code in the function.
To call a function, you write the name of the function,
followed by any necessary information in parentheses.
"""