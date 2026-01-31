"""
You don’t usually need to read through or understand all of
these lines in a traceback.

To handle the error that’s being raised, the try block will
begin with the line that was identified as problematic in the
traceback. In our example, this is the line that contains
read_text():
"""

from pathlib import Path 
path = Path('alice.txt') 

try: 
    contents = path.read_text(encoding='utf-8') 
except FileNotFoundError: 
    print(f"Sorry, the file {path} does not exist.")