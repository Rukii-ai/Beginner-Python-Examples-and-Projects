"""
Often, you’ll want to start with an existing list and make an entirely new list 
based on the first one. To copy a list, you can make a slice that includes the entire original list 
by omitting the first index and the second index ([:]). This tells Python to 
make a slice that starts at the first item and ends with the last item, produc
ing a copy of the entire list.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friends's favourite foos are:")
print(friend_foods)


"""
 If we had simply set friend_foods equal to 
my_foods, we would not produce two separate lists.
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friends's favourite foos are:")
print(friend_foods)

"""
Instead of assigning a copy of my_foods to friend_foods, we set friend_foods 
equal to my_foods. This syntax actually tells Python to associate the new vari
able friend_foods with the list that is already associated with my_foods, so now 
both variables point to the same list. As a result, when we add 'cannoli' to 
my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear 
in both lists, even though it appears to be added only to friend_foods. 
Variables are not containers they're actually just labels to data so 
two variables can labe the same peice of data
"""