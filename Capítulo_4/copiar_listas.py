#Creamos una lista con mis comidas favoritas
my_foods = ["pizza", "cordero", "cochinillo", "churrasco"]
#Creamos otra lista copiando el contenido de la primera
friend_foods = my_foods[:]

#Imprimimos las listas
print("Mis comidas favoritas son:")
print(my_foods)
print("Las comidas favoritas de mi amigo son:")
print(friend_foods)

#Añadimos una comida a cada lista
my_foods.append("cocido")
friend_foods.append("menestra")

#Imprimimos las listas
print("Mis comidas favoritas son:")
for food in my_foods:
    print(food)
print("Las comidas favoritas de mi amigo son:")
for item in friend_foods:
    print(item)