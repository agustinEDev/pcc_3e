from random import randint

class Dado:

    def __init__(self, caras = 6):
        #Crea una instancia de la clase Dado
        self.caras = caras
    
    def tirar_dado(self):
        #Tira el dado e imprime un resultado entre 1 y el número de caras
        caras = self.caras
        print(randint(1, caras))