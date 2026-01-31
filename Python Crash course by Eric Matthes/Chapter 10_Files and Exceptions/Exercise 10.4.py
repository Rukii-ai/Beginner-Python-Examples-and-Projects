from pathlib import Path

path = Path("guest.txt")
path.write_text(input("Hello there guest! What is your name? "))