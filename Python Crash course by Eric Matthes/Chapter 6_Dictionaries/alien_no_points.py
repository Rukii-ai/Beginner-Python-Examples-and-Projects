"""
Using keys in square brackets to retrieve the value you’re
interested in from a dictionary might cause one potential
problem: if the key you ask for doesn’t exist, you’ll get an
error.
"""

alien_0 = {"color": "green", "speed": "slow"}

"""
For dictionaries specifically, you can
use the get() method to set a default value that will be
returned if the requested key doesn’t exist
"""
print(alien_0.get("points", "No point value assigned."))

"""
If there’s a chance the key you’re asking for might not
exist, consider using the get() method instead of the square
bracket notation

If you leave out the second argument in the call to
get() and the key doesn’t exist, Python will return the
value None. The special value None means “no value
exists.” This is not an error: it’s a special value meant
to indicate the absence of a value
"""

print(alien_0.get("points"))