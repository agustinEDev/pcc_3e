#Eliminamos un valor de un diccionario
diccionario = {"nombre" : "agustín", "apellido1" : "estévez", "apellido2" : "domínguez", "edad" : 43}
print(diccionario)
#Recorremos el diccionario para imprimir claves y valores
for k, v in diccionario.items():
    print(f"\nKey: {k.title()}")
    print(f"Value: {v}")

del diccionario["edad"]
print(diccionario)