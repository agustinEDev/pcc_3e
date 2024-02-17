#Inicializamos un diccionario con una lista dentro
pizza = {
    'masa' : 'fina',
    'tamaño' : 'familiar',
    'ingredientes' : ['tomate', 'mozzarella', 'jamón', 'bacon']
}

#Imprimimos por pantalla
print(f"Has pedido una pizza {pizza['tamaño']} de masa {pizza['masa']} con los siguientes ingredientes:")
#bucle para recorrer la lista ingredientes dentro del diccionario pizza
for ingrediente in pizza['ingredientes']:
    print(ingrediente)