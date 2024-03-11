import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

"""Muestra los estilos disponibles para el gráfico"""
#print(plt.style.available)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

#Establece el título del gráfico y las etiquetas de los ejes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize = 14)

plt.show()