import sys
import json
from pathlib import Path
from modulos.file import File
sys.path.append('../files/')

def get_new_username(fichero):
    usuario = input("Introduzca su nombre: ")
    content = json.dumps(usuario)
    fichero.path.write_text(content)
    return usuario

def get_stored_username(fichero):
    if fichero.path.exists():
        contents = fichero.path.read_text()
        usuario = json.loads(contents)
        return usuario
    else:
        return None

def greet_user():
    #Función para saludar al usuario
    fichero = File('../files/username.json')
    username = get_stored_username(fichero)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(fichero)
        print(f"You´ll be remembered, {username}")

greet_user()