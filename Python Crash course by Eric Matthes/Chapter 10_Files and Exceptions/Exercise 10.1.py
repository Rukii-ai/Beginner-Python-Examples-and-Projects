from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()
print(f"{contents}\n")

for line in contents.splitlines():
    print(line)

