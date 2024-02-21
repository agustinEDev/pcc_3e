import os

#Describimos la función para hacer la camiseta
def hacer_camiseta(talla, mensaje=''):
    if mensaje != '':
        print(f"Se fabrica la camiseta talla {talla.upper()} con el mensaje: '{mensaje}'.")
    else:
        print(f"Se fabrica la camiseta talla {talla.upper()}.")

#Describimos la función para seleccionar la talla
def comprobar_talla():
    talla = input("Qué talla es la camiseta que quiere fabricar? ")
    while talla.lower() not in ('xs', 's', 'm', 'l', 'xl', 'xxl'):
        print("No ha introducido una talla válida.")
        talla = input("Qué talla es la camiseta que quiere fabricar? ")
    return talla

#Esta es la función que pregunta si continuamos o no con la aplicación
def continuar():
    repeat = input("Do you want to continue? yes/no: ")
    while repeat not in ('yes','no'):
        print("It is not a valid answer.")
        repeat = input("Do you want to continue? yes/no: ")
    
    if repeat == 'yes':
        return True
    else:
        return False
    
#---------- Inicio del programa ------------------------------------------------
    
flag = True
os.system('clear')
print("Bienvenido a la fábrica de camisetas!")
while flag:
    frase = input("Introduzca la frase a imprimir en la camiseta: ")
    medida = comprobar_talla()

    if frase == '':
        hacer_camiseta(talla = medida)
    else:
        hacer_camiseta(medida, frase)

    flag = continuar()

print("Fin del programa!")

