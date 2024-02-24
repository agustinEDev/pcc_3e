import os
import sys
sys.path.append('../modulos/')
from modulos.file import File
from modulos.switch_flag import set_flag_es

def menu_principal():
    respuesta = 0
    #Función para tratar el menú del programa
    while respuesta not in (1, 2, 3):
        os.system('clear')
        print("---------- Operaciones con ficheros .txt -----------\n")
        print("1. Leer contenido del fichero.")
        print("2. Escribir en el fichero.")
        print("3. Modificar o borrar fichero.")
        print("4. Salir del programa.")
        try:
            #Tratamos el error por si meten alguna opción que haga romper
            respuesta = int(input("\nOpción: "))
        except ValueError:
            respuesta = 0
        if respuesta in (1, 2, 3, 4):
            return respuesta
        else:
            print("No es una opción válida.")
            input("Pulse enter")
            continue

def menu_lectura():
    #Función para mostrar el menú de lectura y leer el fichero
    os.system('clear')
    file = input('Introduce el nombre del fichero que quieres leer: ')
    fichero = File(file)
    os.system('clear')
    fichero.leer_fichero()

def menu_escritura():
    os.system('clear')
    #Función para mostrar el menú de escritura y escribir en el fichero
    file = input('Introduce el nombre del fichero en el que deseas escribir: ')
    cadena = input('Introduce el texto a escribir en el fichero: ')
    fichero = File(file)
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
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres modificar: ')
        cadena = input('Introduce la frase o palabra que quieras modificar: ')
        cadena_new = input('Introduce la frase por la que quieres cambiarla: ')
        fichero = File(file)
        fichero.sustituir_cadena(cadena, cadena_new)
    elif opcion == 2:
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres borrar: ')
        fichero = File(file)
        fichero.sustituir_cadena(fichero.contenido)        
    elif opcion == 3:
        os.system('clear')
        file = input('Introduce el nombre del fichero que quieres eliminar: ')
        fichero = File(file)
        fichero.eliminar_fichero()
        

#------------------ Programa principal ---------------------------------------
opcion = 0
while opcion != 4:
    opcion = menu_principal()
    if opcion == 1:
        menu_lectura()
    elif opcion == 2:
        menu_escritura()
    elif opcion == 3:
        menu_borrado_fichero()
os.system('clear')