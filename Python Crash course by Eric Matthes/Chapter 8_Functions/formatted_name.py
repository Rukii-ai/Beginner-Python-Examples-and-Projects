"""
A function doesn’t always have to display its output directly.
Instead, it can process some data and then return a value or
set of values. The value the function returns is called a
return value. The return statement takes a value from inside
a function and sends it back to the line that called the
function. Return values allow you to move much of your
program’s grunt work into functions, which can simplify the
body of your program.

When you call a function that returns a value, you need to
provide a variable that the return value can be assigned to.
"""

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)