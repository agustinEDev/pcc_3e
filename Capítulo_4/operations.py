squares = []
#Creamos una lista de cuadrados de números entre 1 y 11
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print(f"El mínimo es: {min(squares)}.")
print(f"El máximo es: {max(squares)}.")
print(f"La suma es: {sum(squares)}.")

#Creamos una lista por comprensión
squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)