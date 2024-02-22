from random import randint

class Dados:

    def __init__(self, caras = 6):
        self.caras = caras
    
    def tirar_dado(self):
        caras = self.caras
        print(randint(1, caras))