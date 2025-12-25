alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

"""
As with most new programming concepts, using
dictionaries takes practice. Once you’ve worked with
dictionaries for a bit, you’ll see how effectively they can
model real-world situations

In Python, a dictionary is wrapped in braces ({}) with a
series of key-value pairs inside the braces. A key-value pair is a set of values associated with each
other. When you provide a key, Python returns the value
associated with that key. Every key is connected to its value
by a colon, and individual key-value pairs are separated by
commas. You can store as many key-value pairs as you want
in a dictionary.

To get the value associated with a key, give the name of the
dictionary and then place the key inside a set of square
brackets
"""


new_points = alien_0["points"]
print(f"\nYou just earned {new_points} points!")

"""
Dictionaries are dynamic structures, and you can add new
key-value pairs to a dictionary at any time. To add a new
key-value pair, you would give the name of the dictionary
followed by the new key in square brackets, along with the
new value
"""

print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)


"""
It’s sometimes convenient, or even necessary, to start with
an empty dictionary and then add each new item to it. To
start filling an empty dictionary, define a dictionary with an
empty set of braces and then add each key-value pair on its
own line
"""

alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

"""
Typically, you’ll use empty dictionaries when storing user
supplied data in a dictionary or when writing code that
generates a large number of key-value pairs automatically.

To modify a value in a dictionary, give the name of the
dictionary with the key in square brackets and then the new
value you want associated with that key
"""


alien_0 = {"color": "green"}
print(f"\nThe alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"\nThe alien is now {alien_0['color']}.")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"\nOriginal x-position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its speed.

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:  # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_position"] += x_increment

print(f"New x-position: {alien_0['x_position']}")


"""
When you no longer need a piece of information that’s
stored in a dictionary, you can use the del statement to
completely remove a key-value pair. All del needs is the
name of the dictionary and the key that you want to
remove
"""

alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

"""Be aware that the deleted key-value pair is removed
permanently."""


alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)