import os
os.system('clear')
print("Bienvenido al cine Sotavento!")
print("Para comprar entradas pulse 1.")
print("Para salir pulse 2.")

flag = int(input("Opción: "))
#Comprobamos que sea una opción correcta
while flag != 1 and flag != 2:
    print("Esa no es una opción correcta, pulse 1 o 2.")
    flag = int(input("Opción: "))


while flag != 2:
    os.system('clear')
    edad = int(input("Introduzca su edad: "))
    if edad < 6:
        print("La entrada es gratis.")
    elif edad <=12:
        print("La entrada cuesta 4€.")
    else:
        print("La entrada cuesta 6€.")
    input("Pulse una tecla para continuar...")

    os.system("clear")
    print("\nQué desea hacer?")
    print("Para comprar entradas pulse 1.")
    print("Para salir pulse 2.")
    flag = int(input("Opción: "))
    #Comprobamos que sea una opción correcta
    while flag != 1 and flag != 2:
        print("Esa no es una opción correcta, pulse 1 o 2.")
        flag = int(input("Opción: "))
    
    if flag == 2:
        break
    else:
        continue

os.system("clear")
print("Gracias por venir al cine Sotavento!")
input("Pulse una tecla para continuar...")
