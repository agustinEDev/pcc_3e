#Inicializamos una lista
ingredientes = ["tomate", "jamón", "mozarella", "champiñones"]

if "tomate" in ingredientes:
    print("El tomate está en los ingredientes.")
else:
    print("El tomate no está en los ingredientes")

if "atún" in ingredientes:
    print("El atún está en los ingredientes.")
else:
    print("El atún no está en los ingredientes.")

if ingredientes[0] == "Tomate":
    print("Las cadenas son iguales.")
else:
    print("Las cadenas no son iguales.")

if ingredientes[1] == "jamón":
    print("Las cadenas son iguales.")
else:
    print("Las cadenas no son iguales.")

if ingredientes[0].upper() == "TOMATE":
    print("Las cadenas son iguales.")
else:
    print("Las cadenas no son iguales.")