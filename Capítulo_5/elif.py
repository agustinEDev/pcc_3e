#Utilización de elif

age = 56

if age < 4:
    price = 0
elif age < 16:
    price =  20
else:
    price = 45

print(f"El precio de la suscripción es de {price}€.")