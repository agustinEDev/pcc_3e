pizzas = ["peperoni", "jamón y bacon", "cuatro quesos", "jamón y champiñones"]
friend_pizzas = pizzas[-1:]

pizzas.append("carbonara")
friend_pizzas.append("alcachofas")

print("Me gustan mucho las pizzas...")
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}.")

print("Me encanta la pizza!")

print("A mi amigo le gustan tambien...")
for friend_pizza in friend_pizzas:
    print(f"Le gusta la pizza de {friend_pizza}.")