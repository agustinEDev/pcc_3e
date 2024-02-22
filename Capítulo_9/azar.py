import sys
sys.path.append('../modulos/')
from Capítulo_9.modulos.dado import Dado

tiradas = 10
n = 0

print("--------- Dado 1 ----------")
my_dice = Dado()
while n < tiradas:
    my_dice.tirar_dado()
    n += 1

print("--------- Dado 2 ----------")
n = 0
my_dice2 = Dado(10)
while n < tiradas:
    my_dice2.tirar_dado()
    n += 1

print("--------- Dado 3 ----------")
n = 0
my_dice3 = Dado(20)
while n < tiradas:
    my_dice3.tirar_dado()
    n += 1