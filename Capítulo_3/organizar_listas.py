cars = ["bmw", "audi", "toyota", "subaru"]

#Ordenamos una lista alfabéticamente con la función sort()
cars.sort()
print(cars)
#Ordenamos una lista alfabéticamente a la inversa con sort(reverse=True)
cars.sort(reverse=True)
print(cars)
#Ordenamos la lista temporalmente con la función sorted()
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)

#Creamos una segunda lista
nephews = ["carlos", "eduardo", "javier", "mariana", "diego", "emma", "nico", "susana", "mateo", "jorge", "roque"]
#La ordenamos al contrario con reverse y la imprimimos
nephews.reverse()
print(nephews)
print(f"Tengo {len(nephews)} sobrinos.")

