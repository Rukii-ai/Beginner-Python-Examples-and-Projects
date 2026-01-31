from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ") 
    if first == 'q': 
        break 
    last = input("Please give me a last name: ") 
    if last == 'q': 
        break 
    
    formatted_name = get_formatted_name(first, last) 
    print(f"\tNeatly formatted name: {formatted_name}.")

"""
We can see that the names generated here are correct.
But say we want to modify get_formatted_name() so it can also
handle middle names. 

As we do so, we want to make sure
we don’t break the way the function handles names that
have only a first and last name. We could test our code by
running names.py and entering a name like Janis Joplin
every time we modify get_formatted_name(), but that would
become tedious. 

Fortunately, pytest provides an efficient
way to automate the testing of a function’s output. If we
automate the testing of get_formatted_name(), we can always
be confident that the function will work when given the
kinds of names we’ve written tests for
"""