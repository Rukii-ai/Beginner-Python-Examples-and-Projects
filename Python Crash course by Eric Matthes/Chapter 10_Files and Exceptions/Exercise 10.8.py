from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)
    try:
        contents = path.read_text()

        lines = contents.splitlines()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"\nHere are the contents of the file {filename}:")
        for line in lines:
            print(line)