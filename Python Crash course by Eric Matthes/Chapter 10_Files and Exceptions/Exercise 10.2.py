from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()
modified_lines = []


for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line)


