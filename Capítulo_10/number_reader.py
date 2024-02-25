import json
from pathlib import Path
import sys
sys.path.append('../files/')

from modulos.file import File

#Lo leemos con el read_text de pathlib
path = Path('../files/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)

#Lo leemos desde el contenido de la instancia de File
fichero = File('numbers.json')
numbers2 = json.loads(fichero.contenido)
print(numbers2)