from random import choice

class Boleto():
    #Clase que intenta modelar un boleto de lotería

    def __init__ (self, numero = ''):
        #Instanciamos el boleto
        self.numero = numero
        
    def generar_numero(self):
        #Método que genera el número del boleto con formato 0000-AA
        self.numero = ''
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        letras = ['A', 'E', 'I', 'O', 'U']
        n = 0
        l = 0

        while n < 4:
            self.numero = f"{self.numero}" + choice(numeros)
            n += 1

        self.numero = f"{self.numero}" + '-'

        while l < 2:
            self.numero = f"{self.numero}" + choice(letras)
            l += 1

