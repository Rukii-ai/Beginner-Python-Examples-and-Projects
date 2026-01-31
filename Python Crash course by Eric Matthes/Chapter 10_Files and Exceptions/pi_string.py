from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

"""
When Python reads from a text file, it interprets all
text in the file as a string. If you read in a number and
want to work with that value in a numerical context,
you’ll have to convert it to an integer using the int()
function or a float using the float() function.
"""