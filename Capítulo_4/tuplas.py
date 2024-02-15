#Creamos una tupla que es una como una lista pero en la que no podemos modificar sus elementos
dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

#Sobreescribimos la tupla
dimensions = (400, 100)

for dimension in dimensions:
    print(dimension)