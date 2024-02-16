#Inicializamos la lista de usuarios
usuarios = ["jorge", "félix", "yelena", "admin", "jose antonio", "andré", "diana", "marcos"]

if usuarios:
    for usuario in usuarios:
        if usuario.lower() == "admin":
            print(f"Bienvenido {usuario.title()}, quiere ver los informes?")
        else:
            print(f"Bienvenido {usuario.title()}, gracias por conectarse de nuevo.")
else:
    print("No hay usuarios dados de alta en el sistema.")

print("Fin del programa.")