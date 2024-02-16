available_toppings = ["tomate", "mozzarella", "jamón", "peperoni", "orégano", "aceite de oliva"]
requested_toppings = ["tomate", "mozzarella", "mushrooms", "peperoni"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Añadiendo {requested_topping.title()} a la pizza.")
    else:
        print(f"Lo sentimos, no disponemos de {requested_topping}.")

print("Su pizza ya está en el horno!")