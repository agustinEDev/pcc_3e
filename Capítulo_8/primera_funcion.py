import switch
def greet_user(usuario):
    print(f"Hola {usuario.title()}")

flag = True
while flag:
    #pedimos un nombre por pantalla y lo almacenamos en una variable.
    name = input("Introduce tu nombre: ")
    #Llamamos a la función creada anteriormente
    greet_user(name)
    flag = switch.set_flag_es()