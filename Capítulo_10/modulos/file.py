from pathlib import Path
import os

class File:
    #Clase que intenta modelar un fichero y recibe el nombre del fichero
    def __init__(self, filename):
        self.filename = f"{filename}.txt"
        self.path = Path(f'../files/{self.filename}')
        try:
            #Tratamos el error por si no encuentra el fichero que no rompa
            self.contenido = self.path.read_text()
        except FileNotFoundError:
            print()

    def inicializar (self, filename):
        self.filename = f"{filename}.txt"
        self.path = Path(f'../files/{self.filename}')
        self.contenido = self.path.read_text()


    def escribir_fichero (self, cadena):
        #Método para escribir en el fichero
        if self.path.exists():
            self.contenido += f'\n{cadena}'
            self.path.write_text(self.contenido)
        else:
            self.path.write_text(cadena)


    def leer_fichero (self):
        #Método para leer el contenido del fichero
        if self.path.exists():
            print(self.contenido)
            input("\nPulsa enter para salir... ")
        else:
            print(f"El fichero {self.filename} no existe.")
            input("\nPulsa enter para salir... ")


    def sustituir_cadena (self, cadena, nueva_cadena = ''):
        #Método para borrar una cadena del fichero
        if self.path.exists():
            if cadena in self.contenido:
                if cadena == self.contenido and nueva_cadena == '':
                    self.contenido = self.contenido.replace(
                        f'{cadena}', nueva_cadena
                        )
                else:
                    self.contenido = self.contenido.replace(
                        f'{cadena} ', nueva_cadena)
                    self.contenido = self.contenido.replace(
                        f' {cadena}', nueva_cadena)
                    self.contenido = self.contenido.replace(
                        f'{cadena}', nueva_cadena)
                self.path.write_text(self.contenido)
            else:
                print(f"La cadena {cadena} no existe en el fichero.")
                input('Pulse enter...')
        else:
            print(f"El fichero {self.filename} no existe.")
            input('Pulse enter...')


    def eliminar_fichero (self):
        #Método para eliminar un fichero del directorio
            os.system(f'rm {self.path}')
            input("Fichero borrado")

    def existe(self):
        #Método para comprobar la existencia del fichero
        while self.path.exists() != True:
            print(f"El fichero {self.filename} no existe.")
            try:
                opcion = int(
                    input(
                        "Pulse 1 para introducir otro fichero o 2 para salir: "
                        )
                        )
            except ValueError:
                print("No es un valor válido.")
                continue
            if opcion == 1:
                filename = input("Fichero: ")
                self.inicializar(filename)
                continue
            elif opcion == 2:
                return False
            
        return self.path.exists()
