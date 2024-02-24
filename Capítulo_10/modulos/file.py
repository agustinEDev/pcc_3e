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
        if self.path.exists():
            os.system(f'rm {self.path}')
            input("Fichero borrado")
        else:
            print(f"El fichero {self.filename} no existe.")
            input("Pulse enter... ")
