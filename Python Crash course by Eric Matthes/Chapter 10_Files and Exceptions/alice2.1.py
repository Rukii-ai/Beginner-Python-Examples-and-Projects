"""
You can analyze text files containing entire books. 

Many classic works of literature are available as simple text files
because they are in the public domain. 

The texts used in
this section come from Project Gutenberg (
https://gutenberg.org). 

Project Gutenberg maintains a collection of literary
works that are available in the public domain, and it’s a
great resource if you’re interested in working with literary
texts in your programming projects.
"""

from pathlib import Path 
path = Path('alice_0.txt') 

try: 
    contents = path.read_text(encoding='utf-8') 
except FileNotFoundError: 
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")