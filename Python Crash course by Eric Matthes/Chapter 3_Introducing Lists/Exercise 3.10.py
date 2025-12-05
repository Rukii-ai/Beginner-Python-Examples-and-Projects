rivers = ['Nile', 'Amazon', 'Yangtze', 'Mississippi', 'Danube']

print(rivers[0].title())
print(rivers[1].title())
print(rivers[2].title())
print(rivers[3].title())
print(rivers[4].title())

message = f"The {rivers[0].title()} is the longest river in the world."
print(message)

rivers[1] = 'Congo'
print(rivers)

rivers.append('Ganges')
print(rivers)

rivers.insert(2, 'Mekong')
print(rivers)

del rivers[3]
print(rivers)

irrelevant_river = rivers.pop()
print(irrelevant_river)
print(rivers)

irrelevant_river2 = rivers.pop(2)
print(irrelevant_river2)
print(rivers)

longest_river = 'Nile'
rivers.remove(longest_river)
print(rivers)

print(f"The sorted list of rivers is: {sorted(rivers)}")
print(f"The original list of rivers is: {rivers}")
print(f"The sorted list of rivers in reverse order is: {sorted(rivers, reverse=True)}")
print(f"The original list of rivers is still: {rivers}")
rivers.reverse()
print(f"The list or rivers in reverse order is: {rivers}")
rivers.reverse()
print(f"The list of rivers after reversing again is: {rivers}")
rivers.sort()
print(f"The list of rivers sorted permamently is: {rivers}")
rivers.sort(reverse=True)
print(f"The list of rivers sorted in reverse order permanently is: {rivers}")
print(f"The number of rivers in the list is: {len(rivers)}")

"""
I had a bug in that the following lines outputted None instead of the river names:
print(f"The list or rivers in reverse order is: {rivers.reverse()}") 
print(f"The list of rivers after reversing again is: {rivers.reverse()}") 
print(f"The list of rivers sorted permamently is: {rivers.sort()}") 
print(f"The list of rivers sorted in reverse order permanently is: {rivers.sort(reverse=True)}")

And the reason for that is the list methods I was calling:
reverse()
sort()
Do not return the modified list.
They modify the list in place and return None.

Python list methods like .reverse() and .sort() are designed to:
1) Change the original list
2) Return None to make sure I don’t mistakenly think they return a new list

So when I write:
print(rivers.reverse())

I am printing the return value of .reverse(), which is always:
None
"""
