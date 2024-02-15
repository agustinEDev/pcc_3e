#Inicializamos una lista
cars = ["audi", "bmw", "ford", "toyota", "citroen"]
#Recorremos la lista con un for para imprimirla y si es BMW todo en mayúsculas
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())