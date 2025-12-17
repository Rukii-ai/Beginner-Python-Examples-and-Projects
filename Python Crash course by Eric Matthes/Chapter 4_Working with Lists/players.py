"""
You can also work with a specific group of items in a list, called a slice in 
Python
"""

"""
To make a slice, you specify the index of the first and last elements you want 
to work with. As with the range() function, Python stops one item before the 
second index you specify.
"""


players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

"""
You can generate any subset of a list
"""

print(players[1:4])

"""
If you omit the first index in a slice, Python automatically starts your 
slice at the beginning of the list
"""

print(players[:4])

"""
A similar syntax works if you want a slice that includes the end of a list.This syntax allows you to output all of the elements from any point in 
your list to the end, regardless of the length of the list.  
"""

print(players[2:])

"""
Recall that a nega
tive index returns an element a certain distance from the end of a list; 
therefore, you can output any slice from the end of a list
"""

print(players[-3:])

"""
You can include a third value in the brackets indicating a slice. If a third value is 
included, this tells Python how many items to skip between items in the specified 
range
"""

"""
You can use a slice in a for loop if you want to loop through a subset of the 
elements in a list
"""

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
for player in players[:3]:
    print(f"{player.title()}")


"""
Slices are very useful in a number of situations. For instance, when 
you’re creating a game, you could add a player’s final score to a list every 
time that player finishes playing. You could then get a player’s top three 
scores by sorting the list in decreasing order and taking a slice that includes 
just the first three scores. When you’re working with data, you can use slices 
to process your data in chunks of a specific size. Or, when you’re building 
a web application, you could use slices to display information in a series of 
pages with an appropriate amount of information on each page
"""