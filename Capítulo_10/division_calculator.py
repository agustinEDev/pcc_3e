print("Introduce dos número para dividirlos.")
print("Pulsa 'q' para salir.")

while True:
    first_number = input("\nIntroduce el primer número: ")
    if first_number == 'q':
        break
    second_number = input("Introduce el número por el que quieras dividir: ")
    if second_number == 'q':
        break
    try:
        resultado = int(first_number) / int(second_number)
        print(f"El resultado es: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except ValueError:
        print("Valores erroneos.")