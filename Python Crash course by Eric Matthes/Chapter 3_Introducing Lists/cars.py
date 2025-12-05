"""
 Python’s sort() method makes it relatively easy to sort a list
 """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

"""
 The sort() method changes the order of the list
 permanently. The cars are now in alphabetical order, and we
 can never revert to the original order
"""

"""
You can also sort this list in reverse-alphabetical order by
 passing the argument reverse=True to the sort() method
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

"""
 To maintain the original order of a list but present it in a
 sorted order, you can use the sorted() function. The sorted()
 function lets you display your list in a particular order, but
 doesn’t affect the actual order of the list. The sorted() function
 can also accept a reverse=True argument if you want to
 display a list in reverse-alphabetical order.
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here is the original list: \n\t{cars}")

print(f"Here is the sorted list: \n\t{sorted(cars)}")
print(f"Here is the original list again: \n\t{cars}")
print(f"Here is the reverse sorted list: \n\t{sorted(cars, reverse=True)}")
print(f"Here is the original list again: \n\t{cars}")

"""
.sort() is a method while sorted() is a function and both receive arguments.
"""

"""
To reverse the original order of a list, you can use the
 reverse() method. reverse() doesn’t sort backward alphabetically;
 it simply reverses the order of the list.  The reverse() method changes the order of a list
 permanently, but you can revert to the original order
 anytime by applying reverse() to the same list a second
 time.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

"""
 You can quickly find the length of a list by using the len()
 function.  You’ll find len() useful when you need to identify the
 number of aliens that still need to be shot down in a game,
 determine the amount of data you have to manage in a
 visualization, or figure out the number of registered users on
 a website, among other tasks
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))