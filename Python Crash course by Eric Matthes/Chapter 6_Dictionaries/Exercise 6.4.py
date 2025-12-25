glossary ={
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'Work through a collection of items, one at a time.',
    'tuple': 'A collection of items in a particular order that cannot be changed.',
    'set': 'A collection of unique items.',
    'method': 'A function that is associated with an object.',
    'function': 'A block of code that performs a specific task.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'The second item in a key-value pair in a dictionary.'
    }

print("A few programming terms explained:")

for key in glossary:
    print(f"{key.title()}: \n\t{glossary[key]}\n")