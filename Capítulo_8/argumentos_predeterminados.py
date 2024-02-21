#Esta es la función que monta la frase dependiendo de los argumentos que lleguen
def desc_pet (name, type = 'dog'):
    print(f"I have a {type.lower()} named {name.title()}.")

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

#------------------ Inicio del programa ----------------------------------------
#Ponemos de entrada el flag a true para que entre en el bucle
#El flag se seteará después al llamar a la función continuar
flag = True

while flag:
    type = input("What kind of pet do you have? ")
    name = input("What is your pet´s name? ")
    #Dependiendo del tipo de mascota, enviamos uno o dos parámetros
    if type.lower() != 'dog':
        desc_pet(name, type)
    else:
        desc_pet(name)
    #Llamamos a la función continuar para setear el flag
    flag = continuar()

print("Fin del programa!")