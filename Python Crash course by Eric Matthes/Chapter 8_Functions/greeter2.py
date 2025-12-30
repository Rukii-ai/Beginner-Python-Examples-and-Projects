def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

"""
By adding username here, you allow the function
to accept any value of username you specify. The function now
expects you to provide a value for username each time you
call it.

The variable username in the definition of greet_user() is an
example of a parameter, a piece of information the function
needs to do its job. The value 'jesse' in greet_user('jesse') is
an example of an argument. An argument is a piece of
information that’s passed from a function call to a function.
When we call the function, we place the value we want the
function to work with in parentheses. In this case the
argument 'jesse' was passed to the function greet_user(),
and the value was assigned to the parameter username.

People sometimes speak of arguments and
parameters interchangeably. Don’t be surprised if you
see the variables in a function definition referred to as
arguments or the variables in a function call referred
to as parameters.
"""

greet_user('sarah')

