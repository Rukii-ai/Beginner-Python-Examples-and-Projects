from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try: 
        contents = path.read_text(encoding='utf-8') 
    except FileNotFoundError: 
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path('alice_0.txt')
count_words(path)

"""
It’s a good habit
to keep comments up to date when you’re modifying a
program, so the comment has also been changed to a
docstring and reworded slightly.
"""