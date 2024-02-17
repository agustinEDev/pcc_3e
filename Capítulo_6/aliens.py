#Creamos una lista vacía para almacenar los aliens
aliens = []

#Creamos 30 aliens(diccionarios) y los almacenamos en una lista
for number in range(30):
    new_alien = {'color' : 'verde', 'puntos' : 5, 'velocidad' : 'slow'}
    aliens.append(new_alien)

#Modificamos los 3 primeros aliens
for alien in aliens[:3]:
    if alien['color'] == 'verde':
        alien['color'] = 'amarillo'
        alien['puntos'] = 10
        alien['velocidad'] = 'medium'

#Imprimimos los primeros 5 aliens de la lista
for alien in aliens[:5]:
    print(alien)
print("...")

#Imprimimos la cantidad de aliens creados en la lista aliens
print(f"Número de aliens creados: {len(aliens)}")