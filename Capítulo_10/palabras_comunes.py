from modulos.file import File
import pathlib
import sys
sys.path.append("../files/")

fichero = File('moby_dick.txt')
print(f"La palabra 'row' sale en {fichero.filename} {fichero.contenido.lower().count('whale')} veces.")