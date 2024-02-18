bocadillos_disponibles = ['atún','pastrami','jamón y queso','chorizo', 'pastrami','bacon','pastrami','nocilla']
bocadillos_terminados = []

print("Ya no queda pastrami.")
while 'pastrami' in bocadillos_disponibles:
    bocadillos_disponibles.remove('pastrami')

while bocadillos_disponibles:
    bocadillo = bocadillos_disponibles.pop()
    print(f"Su bocadillo de {bocadillo.title()} está listo.")
    bocadillos_terminados.append(bocadillo)

print("------- Bocadillos realizados --------")
print(bocadillos_terminados)