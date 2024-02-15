#Imprimimos los números del 1 al 20
for value in range(1, 21):
    print(value)
#Creamos una lista con los número del 1 al millón y lo imprimimos con bucle for
millions = list(range(1, 1000001))
for million in millions:
    print(million)
#Imprimimos el mínimo, el máximo y la suma de la lista anterior
print(f"El mínimo es: {min(millions)}")
print(f"El máximo es: {max(millions)}")
print(f"La suma de todos los números de la lista es: {sum(millions)}")
#Creamos una lista de los impares del 1 al 20 e imprimimos con blucle for
impares = list(range(1,20,2))
for impar in impares:
    print(impar)
#Creamos una lista con los multiplos de 3 desde el 3 hasta el 30 y la imprimimos
multiplos = list(range(3, 31, 3))
for multiplo in multiplos:
    print(multiplo)
#Creamos una lista con los cubos de los números del 1 al 10 y lo imprimimos
cubos = [value ** 3 for value in range(1,10)]
for cubo in cubos:
    print(cubo)