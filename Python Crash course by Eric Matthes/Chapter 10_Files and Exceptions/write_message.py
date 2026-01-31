"""
One of the simplest ways to save data is to write it to a file.

When you write text to a file, the output will still be
available after you close the terminal containing your
program’s output. 

You can examine output after a program
finishes running, and you can share the output files with
others as well.

You can also write programs that read the
text back into memory and work with it again later.

Once you have a path defined, you can write to a file using
the write_text() method.
"""


from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming")


"""
The write_text() method takes a single argument: the
string that you want to write to the file. 

This program has no
terminal output, but if you open the file programming.txt,
you’ll see one line.

This file behaves like any other file on your computer. You
can open it, write new text in it, copy from it, paste to it,
and so forth.

Python can only write strings to a text file. If you want
to store numerical data in a text file, you’ll have to
convert the data to string format first using the str()
function.
"""