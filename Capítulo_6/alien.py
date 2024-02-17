#Trabajamos con el primer diccionario
alien_0 = {"color" : "verde", "puntos" : 5}

#Imprimimos los valores asociados a las claves color y puntos
print(alien_0["color"])
print(alien_0["puntos"])

#Añadimos dos nuevos pares clave-valor
alien_0["x_position"] = 0
alien_0["y_position"] = 25

#Imprimimos el diccionario entero
print(alien_0)

#Modificamos un valor del diccionario
print(f"El alien es de color {alien_0['color']}.")
alien_0["color"] = "amarillo"
print(f"El alien es de color {alien_0['color']}.")