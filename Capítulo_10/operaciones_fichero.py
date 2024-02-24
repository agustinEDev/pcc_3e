import os
import pathlib
import sys
sys.path.append('../modulos/')
from modulos.file import File
from modulos.switch_flag import set_flag_es

def menu_principal():
    respuesta = 0
    #Función para tratar el menú del programa
    while respuesta not in (1, 2, 3, 4, 5):
        os.system('clear')
        print("---------- Operaciones con ficheros .txt -----------\n")
        print("1. Leer contenido del fichero.")
        print("2. Escribir en el fichero.")
        print("3. Modificar o borrar fichero.")
        print("4. Listar ficheros.")
        print("5. Salir del programa.")
        try:
            #Tratamos el error por si meten alguna opción que haga romper
            respuesta = int(input("\nOpción: "))
        except ValueError:
            respuesta = 0
        if respuesta in (1, 2, 3, 4, 5):
            return respuesta
        else:
            print("No es una opción válida.")
            input("Pulse enter")
            continue

def menu_lectura():
    #Función para mostrar el menú de lectura y leer el fichero
    os.system('clear')
    file = input('Introduce el nombre del fichero que quieres leer: ')
    fichero = File(file.lower())
    os.system('clear')
    if fichero.existe():
        fichero.leer_fichero()

def menu_escritura():
    os.system('clear')
    file = ''
    #Función para mostrar el menú de escritura y escribir en el fichero
    print("En caso de no existir, se creará el fichero.\n")
    while file == '':
        file = input(
            'Introduce el nombre del fichero en el que deseas escribir: ')
    cadena = input('Introduce el texto a escribir en el fichero: ')
    fichero = File(file.lower())
    fichero.escribir_fichero(cadena)

def menu_borrado_fichero():
    #Función para mostrar el menú de borrado y borrar el fichero
    os.system('clear')
    print("1. Modificar frase o palabra.")
    print("2. Borrar fichero entero.")
    print("3. Eliminar fichero.")
    print("4. Salir.")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Opción incorrecta.")
        input("Pulsa enter... ")
    if opcion == 1:
        #Modificación de un fichero existente
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres modificar: ')
        fichero = File(file.lower())
        if fichero.existe():
            cadena = input('Introduce la frase o palabra que quieras modificar: ')
            cadena_new = input('Introduce la frase por la que quieres cambiarla: ')
            fichero.sustituir_cadena(cadena, cadena_new)
    elif opcion == 2:
        #Borra el contenido de un fichero existente
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres borrar: ')
        fichero = File(file.lower())
        if fichero.existe():
            fichero.sustituir_cadena(fichero.contenido)        
    elif opcion == 3:
        #Elimina un fichero existente
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres eliminar: ')
        fichero = File(file.lower())
        if fichero.existe():
            fichero.eliminar_fichero()

def menu_listar():
    #Función para listar los archivos txt del directorio con el que trabajamos
    os.system('clear')
    p = pathlib.Path('/Users/agustined/Desktop/python_work/files/')
    print("------------- Ficheros en el directorio -------------------\n")
    for file in p.glob('*.txt'):
        file = f"{file}"
        print(file.removeprefix('/Users/agustined/Desktop/python_work/files/'))
    input("\nPulse enter para salir...")
        

#------------------ Programa principal ---------------------------------------
opcion = 0
while opcion != 5:
    opcion = menu_principal()
    if opcion == 1:
        menu_lectura()
    elif opcion == 2:
        menu_escritura()
    elif opcion == 3:
        menu_borrado_fichero()
    elif opcion == 4:
        menu_listar()
os.system('clear')
