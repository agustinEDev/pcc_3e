alien_0 = {"x_position" : 0, "y_position" : 10, "speed" : "medium"}
print(f"El alien originalmente está en la posición: {alien_0['x_position']}")

alien_0["speed"] = "fast"
#dependiendo de la velocidad, marcaremos un incremento para luego sumar a x
if alien_0["speed"] == "low":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"El alien ahora está en la posición: {alien_0['x_position']}")