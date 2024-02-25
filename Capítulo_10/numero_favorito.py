import json
import sys
sys.path.append('../files/')
from pathlib import Path
from modulos.file import File

def get_new_favorite_number (file):
    number = input("Enter your favorite number: ")
    content = json.dumps(number)
    file.path.write_text(content)
    return number

def get_favorite_number ():
    file = File('favorite_number.json')
    if file.path.exists():
        content = file.path.read_text()
        number = json.loads(content)
        print(f"Your favorite number is {number}")
    else:
        number = get_new_favorite_number(file)
        print(f"Your number will be remembered.")

get_favorite_number()