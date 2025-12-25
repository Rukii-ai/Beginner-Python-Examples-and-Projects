"""
Python refers to values that cannot change as immutable,
and an immutable list is called a tuple
"""

"""
A tuple looks just like a list, except you use parentheses
instead of square brackets. Once you define a tuple, you can
access individual elements by using each item’s index, just
as you would for a list.
"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""
Tuples are technically defined by the presence of a
comma; the parentheses make them look neater and
more readable. If you want to define a tuple with one
element, you need to include a trailing comma

It doesn’t often make sense to build a tuple with one
element, but this can happen when tuples are
generated automatically.
"""

my_t = (3,)
print(my_t)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimesions")
for dimension in dimensions:
    print(dimension)