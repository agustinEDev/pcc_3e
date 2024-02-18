current_number = 0
#Con continue salta todo lo que hay después pero sigue en el bucle
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

current_number = 0
#Con break sale del bucle
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        break
    print(current_number)

print("Fin del programa.")