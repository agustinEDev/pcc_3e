#Inicializamos una lista con ingredientes para una pizza
ingredientes = ["tomate", "mozzarella", "jamón", "peperoni", "orégano", "aceite de oliva"]

if ingredientes:
    for ingrediente in ingredientes:
        if ingrediente.lower() == "peperoni":
            print(f"Lo sentimos, no queda {ingrediente.title()}.")
        else:
            print(f"Añadiendo {ingrediente.title()} a la pizza.")
else:
    print("Está seguro de querer una pizza vacía?")

print("Su pizza ya está en el horno!")