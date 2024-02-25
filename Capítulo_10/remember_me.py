import json
import sys
sys.path.append('../files/')
from modulos.file import File

fichero = File('username.json')
if fichero.path.exists():
    contenido = json.loads(fichero.contenido)
    print(f"Bienvenido de nuevo, {contenido}!")
else:
    nombre = input("Cuál es tu nombre? ")   
    username = json.dumps(nombre)
    fichero.path.write_text(username)
    print(f"Te recordaremos cuando vuelvas, {nombre}")