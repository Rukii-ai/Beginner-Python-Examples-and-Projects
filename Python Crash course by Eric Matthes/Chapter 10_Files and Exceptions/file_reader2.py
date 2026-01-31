"""
When you’re working with a file, you’ll often want to
examine each line of the file. You might be looking for
certain information in the file, or you might want to modify
the text in the file in some way.

For example, you might
want to read through a file of weather data and work with
any line that includes the word sunny in the description of
that day’s weather.

In a news report, you might look for any
line with the tag <headline> and rewrite that line with a
specific kind of formatting.

You can use the splitlines() method to turn a long string
into a set of lines, and then use a for loop to examine each
line from a file, one at a time:
"""

from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line)



"""
After you’ve read the contents of a file into memory, you
can do whatever you want with that data
"""