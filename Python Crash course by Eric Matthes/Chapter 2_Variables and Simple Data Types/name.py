name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

"""A method is a function that is associated with a particular object. 
In this case, the object is name, which is a string, and the method is title(). 
The title() method returns a version of the string where the first letter of each word is capitalized.
 A method is an action that
 Python can perform on a piece of data. The dot (.) after name
 in name.title() tells Python to make the title() method act
 on the variable name. Every method is followed by a set of
 parentheses, because methods often need additional
 information to do their work. That information is provided
 inside the parentheses. The title() function doesn’t need
 any additional information, so its parentheses are empty.
  The lower() method is particularly useful for storing data.
 You typically won’t want to trust the capitalization that your
 users provide, so you’ll convert strings to lowercase before
 storing them. Then when you want to display the
 information, you’ll use the case that makes the most sense
 for each string
"""