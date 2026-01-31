from pathlib import Path
import json

path = Path('favourite_number.json')

favourite_number = input("Enter your favourite number? ")
path.write_text(json.dumps(favourite_number))