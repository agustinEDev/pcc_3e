def suma(numero_1, numero_2):
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except ValueError:
        print ("Algún valor introducido es erróneo.")
        return True
    else:
        suma = numero_1 + numero_2
        print(f"El resultado de la suma es: {suma}")
        return False


#--------------------------------------------------
flag = True
while flag:
    numero1 = input("Introduce el primer número: ")
    numero2 = input("Introduce el segundo número: ")
    flag = suma(numero1, numero2)