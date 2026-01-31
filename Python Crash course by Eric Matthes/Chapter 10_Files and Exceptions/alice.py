"""
One common issue when working with files is handling
missing files. 

The file you’re looking for might be in a
different location, the filename might be misspelled, or the
file might not exist at all. 

You can handle all of these situations with a try-except block.
"""

from pathlib import Path

path = Path("alice.txt")
contents = path.read_text(encoding='utf-8')

"""
Note that we’re using read_text() in a slightly different way
here than what you saw earlier. 

The encoding argument is
needed when your system’s default encoding doesn’t match
the encoding of the file that’s being read. 

This is most likely
to happen when reading from a file that wasn’t created on
your system

Python can’t read from a missing file, so it raises an
exception:

Traceback (most recent call last): 
  File "alice.py", line 4, in <module> 
    contents = path.read_text(encoding='utf-8') 
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
  File "/.../pathlib.py", line 1056, in read_text 
    with self.open(mode='r', encoding=encoding, errors=errors) as f: 
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
  File "/.../pathlib.py", line 1042, in open 
    return io.open(self, mode, buffering, encoding, errors, newline) 
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'



This is a longer traceback than the ones we’ve seen
previously, so let’s look at how you can make sense of more
complex tracebacks. 

It’s often best to start at the very end
of the traceback. 

On the last line, we can see that a
FileNotFoundError exception was raised. 

This is important
because it tells us what kind of exception to use in the
except block that we’ll write.

Looking back near the beginning of the traceback, we
can see that the error occurred at line 4 in the file alice.py.
The next line shows the line of code that caused the error.
The rest of the traceback shows some code from the libraries 
that are involved in opening and reading from files.

"""

