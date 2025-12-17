"""
Many reasons exist to store a set of numbers. For example, you’ll need to 
keep track of the positions of each character in a game, and you might want 
56   Chapter 4
Working with Lists   57
to keep track of a player’s high scores as well. In data visualizations, you’ll 
almost always work with sets of numbers, such as temperatures, distances, 
population sizes, or latitude and longitude values, among other types of 
numerical sets.
Lists are ideal for storing sets of numbers, and Python provides a variety 
of tools to help you work efficiently with lists of numbers. Once you under
stand how to use these tools effectively
"""

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

for value in range(6):
    print(value)


"""
If you want to make a list of numbers, you can convert the results of range() 
directly into a list using the list() function. When you wrap list() around a 
call to the range() function, the output will be a list of numbers
"""

numbers = list(range(1, 6))
print(numbers)