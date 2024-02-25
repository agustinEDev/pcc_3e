from modulos.file import File
import sys
import pathlib
sys.path.append("../files/")

fichero1 = File('perros.txt')
fichero2 = File('gatos.txt')
try:
    fichero1.leer_fichero()
    fichero2.leer_fichero()
except FileNotFoundError:
    #print('Uno de los ficheros no se encuentra.')
    pass