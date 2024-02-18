import os
respuestas = {}
flag = True

while flag:
    name = input("Introduzca su nombre: ")
    country = input("A dónde te gustaría viajar? ")
    #Almacenamos en el dicccionario el nombre y el país
    respuestas[name] = country
    os.system('clear')
    repeat = input("Quiere seguir con la encuesta? (si/no) ")
    while repeat not in ('si', 'no'):
        print("No es una respuesta válida.")
        repeat = input("Quiere seguir con la encuesta? (si/no) ")

    if repeat == 'no':
        flag = False

print("---------- Encuesta terminada ----------")
for name, country in respuestas.items():
    print(f"A {name.title()} le gustaría viajar a {country.title()}.")

print("\nFin del programa.")

