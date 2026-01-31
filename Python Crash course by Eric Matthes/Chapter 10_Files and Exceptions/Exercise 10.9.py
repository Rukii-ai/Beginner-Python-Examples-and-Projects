from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)
    try:
        contents = path.read_text()

        lines = contents.splitlines()
    except FileNotFoundError:
        pass
    else:
        print(f"Here are the contents of the file {filename}:")
        for line in lines:
            print(line)