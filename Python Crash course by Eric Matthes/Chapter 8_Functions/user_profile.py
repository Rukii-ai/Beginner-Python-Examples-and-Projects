"""
Sometimes you’ll want to accept an arbitrary number of
arguments, but you won’t know ahead of time what kind of
information will be passed to the function. In this case, you
can write functions that accept as many key-value pairs as
the calling statement provides. One example involves
building user profiles: you know you’ll get information about
a user, but you’re not sure what kind of information you’ll
receive. The function build_profile() in the following
example always takes in a first and last name, but it accepts
an arbitrary number of keyword arguments as well
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile("albert", "einstein", 
                             location="Princeton",
                             field="physics")

print(user_profile)

"""
You can mix positional, keyword, and arbitrary values in
many different ways when writing your own functions. It’s
useful to know that all these argument types exist because
you’ll see them often when you start reading other people’s
code. It takes practice to use the different types correctly
and to know when to use each type. For now, remember to
use the simplest approach that gets the job done. As you
progress, you’ll learn to use the most efficient approach
each time.

You’ll often see the parameter name **kwargs used to
collect nonspecific keyword arguments.
"""

