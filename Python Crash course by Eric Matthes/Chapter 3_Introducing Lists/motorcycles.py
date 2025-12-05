motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

"""
The simplest way to add a new element to a list is to
 append the item to the list. When you append an item to a
 list, the new element is added to the end of the list.
"""

motorcycles.append('honda')
print(motorcycles)

motorcycles = []  # Start with an empty list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

"""
 You can add a new element at any position in your list by
 using the insert() method. You do this by specifying the
 index of the new element and the value of the new item
"""

motorcycles.insert(1, 'ducati')
print(motorcycles)

"""
 If you know the position of the item you want to remove
 from a list, you can use the del statement. You can no longer access the value that
 was removed from the list after the del statement is used.
 del is a statement
"""

del motorcycles[1]
print(motorcycles)

"""
Sometimes you’ll want to use the value of an item after you
 remove it from a list. For example, you might want to get
 the x and y position of an alien that was just shot down, so
 you can draw an explosion at that position. In a web
 application, you might want to remove a user from a list of
 active members and then add that user to a list of inactive
 members.

The pop() method removes the last item in a list, but it lets
 you work with that item after removing it. The term pop
 comes from thinking of a list as a stack of items and
 popping one item off the top of the stack. In this analogy,
 the top of a stack corresponds to the end of a list
 .pop() is a method
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print(f"I last owned a {popped_motorcycles.title()} motorcycle in my 20's")

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {last_owned.title()}.")

"""
 If you’re unsure whether to use the del statement or the
 pop() method, here’s a simple way to decide: when you want
 to delete an item from a list and not use that item in any
 way, use the del statement; if you want to use an item as
 you remove it, use the pop() method
"""


"""
Sometimes you won’t know the position of the value you
 want to remove from a list. If you only know the value of the
 item you want to remove, you can use the remove() method
"""


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

"""
You can also use the remove() method to work with a value
 that’s being removed from a list.
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for him.")

"""
The remove() method deletes only the first occurrence
 of the value you specify. If there’s a possibility the
 value appears more than once in the list, you’ll need
 to use a loop to make sure all occurrences of the
 value are removed
"""