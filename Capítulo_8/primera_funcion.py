
def greet_user(usuario):
    print(f"Hola {usuario.title()}")

#pedimos un nombre por pantalla y lo almacenamos en una variable.
name = input("Introduce tu nombre: ")
#Llamamos a la función creada anteriormente
greet_user(name)