#Inicializamos un diccionario con listas como valores
favorite_fruit = {
    'josé' : ['fresa', 'plátano'],
    'nuria' : ['kiwi', 'manzana', 'naranja'],
    'ana' : ['melón', 'melocotón'],
    'josesiño' : ['uva']
}
#Con el primer for recorremos el diccionario y con el segundo cada lista
for name, fruits in favorite_fruit.items():
    if len(fruits)>1:
        print(f"Las frutas favoritas de {name.title()} son: ")
    else:
        print(f"La fruta favorita de {name.title()} es: ")
    
    for fruit in fruits:
        print(fruit)
    print("\n")