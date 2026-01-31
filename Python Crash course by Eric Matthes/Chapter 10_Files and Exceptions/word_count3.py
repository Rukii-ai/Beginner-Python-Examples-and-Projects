""" 
Sometimes, you’ll want the program to
fail silently when an exception occurs and continue on as if
nothing happened.

To make a program fail silently, you write
a try block as usual, but you explicitly tell Python to do
nothing in the except block. Python has a pass statement that
tells it to do nothing in a block
"""


from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try: 
        contents = path.read_text(encoding='utf-8') 
    except FileNotFoundError: 
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ["alice_0.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)

"""
The only difference between this listing and the previous
one is the pass statement in the except block. 

Now when a
FileNotFoundError is raised, the code in the except block runs,
but nothing happens. 

No traceback is produced, and there’s
no output in response to the error that was raised. 

Users see
the word counts for each file that exists, but they don’t see
any indication that a file wasn’t found:

The pass statement also acts as a placeholder. It’s a
reminder that you’re choosing to do nothing at a specific
point in your program’s execution and that you might want
to do something there later. 

For example, in this program we
might decide to write any missing filenames to a file called
missing_files.txt. Our users wouldn’t see this file, but we’d
be able to read the file and deal with any missing texts.

How do you know when to report an error to your users and
when to let your program fail silently? 

If users know which
texts are supposed to be analyzed, they might appreciate a
message informing them why some texts were not
analyzed. 

If users expect to see some results but don’t know
which books are supposed to be analyzed, they might not
need to know that some texts were unavailable. Giving
users information they aren’t looking for can decrease the
usability of your program. 

Python’s error-handling structures
give you fine-grained control over how much to share with
users when things go wrong; it’s up to you to decide how
much information to share.

Well-written, properly tested code is not very prone to
internal errors, such as syntax or logical errors. But every
time your program depends on something external such as
user input, the existence of a file, or the availability of a
network connection, there is a possibility of an exception
being raised. 

A little experience will help you know where to
include exception-handling blocks in your program and how
much to report to users about errors that arise
"""