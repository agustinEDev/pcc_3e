motos = ["Honda", "Piaggio", "Suzuki"]
print(motos)
#Modificamos el primer elemento de la lista
motos[0]="Ducatti"
print(motos)
#Añadimos un nuevo elemento al final de la lista
motos.append("Honda")
print(motos)
#Insertamos un elemento en una posición determinada
motos.insert(0, "Yamaha")
print(motos)
#Eliminamos un elemento en una posición determinada
del motos[0]
print(motos)
#Eliminar el último elemento con el método pop() y lo imprimimos después
popped_moto = motos.pop()
print(motos)
print(popped_moto)
#Eliminar un elemento determinado de la lista con el método pop() y lo imprimimos
first_element = motos.pop(0)
print(motos)
print(first_element.title())
#Eliminar un elemento por su valor con el método pop() y lo imprimimos
motos.remove('Piaggio')
print(motos)

#Rellenamos la lista y operamos con remove
motos.append("Piaggio")
motos.insert(0,  "Ducatti")
motos.insert(2, "Honda")
print(motos)

too_expensive = "Suzuki"
motos.remove(too_expensive)
print(motos)
print(f"La marca {too_expensive.title()} es demasiado cara para mi.")