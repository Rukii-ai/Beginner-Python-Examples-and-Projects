"""
Sometimes it makes sense to make an argument optional,
so that people using the function can choose to provide
extra information only if they want to. You can use default
values to make an argument optional.
"""

def formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)

musician = formatted_name('john', 'hooker', 'lee')
print(musician)

"""
In this example, the name is built from three possible
parts. Because there’s always a first and last name, these
parameters are listed first in the function’s definition. The
middle name is optional, so it’s listed last in the definition,
and its default value is an empty string.

Optional values allow functions to handle a wide range of
use cases while letting function calls remain as simple as
possible.
"""