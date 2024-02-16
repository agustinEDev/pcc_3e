#Eliminamos un valor de un diccionario
diccionario = {"nombre" : "agustín", "apellido1" : "estévez", "apellido2" : "domínguez", "edad" : 43}
print(diccionario)

del diccionario["edad"]
print(diccionario)