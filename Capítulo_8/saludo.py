def saludo (nombre):
    print(f"Hola {nombre.title()}")

print("Bienvenido a Sotavento!")
flag = True
while flag:
    name = input("Introduzca su nombre: ")
    saludo(name)

    repeat = input("Quiere introducir otro nombre? si/no: ")
    while repeat not in ('si','no'):
        print("No es una respuesta váida.")
        repeat = input("Quiere introducir otro nombre? (si/no): ")

    if repeat == 'no':
        flag = False

print("Fin del programa 'saludo.py'.")