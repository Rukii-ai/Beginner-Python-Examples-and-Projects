"""
A function can return any kind of value you need it to,
including more complicated data structures like lists and
dictionaries.
"""

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person_2(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {}
    person['first'] = first_name
    person['last'] = last_name
    return person

musician = build_person_2('jimi', 'hendrix')
print(musician)




first_names =['jimi', 'john', 'miles', 'charlie', 'dizzy', 'thelonious']
last_names = ['hendrix', 'hooker', 'davis', 'parker', 'gillespie', 'monk']

"""
zip() is a built-in Python function used to loop through two or more lists
at the same time. It takes one item from each list and groups them together.

For example, the first item in the first list is paired with the first item
in the second list, the second with the second, and so on.

The loop stops when the shortest list runs out of items.
"""

for first, last in zip(first_names, last_names):
    musician = build_person(first, last)
    print(musician)

