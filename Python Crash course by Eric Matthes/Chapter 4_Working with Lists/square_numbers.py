"""
You can create almost any set of numbers you want to using the range() 
function. For example, consider how you might make a list of the first 10 
square numbers (that is, the square of each integer from 1 through 10). In 
Python, two asterisks (**) represent exponents.
"""


squares =[]

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)


"""
To write this code more concisely, omit the temporary variable square 
and append each new value directly to the list
"""


squares =[]

for value in range(1, 11):
    squares.append(value**2)

print(squares)

"""
Sometimes using a temporary variable makes your code easier to 
read; other times it makes the code unnecessarily long. Focus first on writ
ing code that you understand clearly, and does what you want it to do. Then 
look for more efficient approaches as you review your code
"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
