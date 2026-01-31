from pathlib import Path

files = ["frankenstein.txt", "romeo and julliet.txt", "crime and punishment.txt"]

for filename in files:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')

        lines = contents.splitlines()
    except FileNotFoundError:
        pass
    else:
        print(f"\nThe number of times 'the' appears in the file {filename} is:")
        count = 0
        for line in lines:
            count += line.count('the')
        print(count)
        
        print("\nAccounting for different cases we have:")
        count = 0
        for line in lines:
            count += line.lower().count('the')
        print(count)
        
        print("\nNot counting the words have 'the' as their beginnings we have:")
        count = 0
        for line in lines:
            count += line.count(' the ')
        print(count)
        