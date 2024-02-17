favorite_languages = {
    "Agustín" : "Python",
    "José" : "C#",
    "Nuria" : "Java",
    "Ana" : "HTML",
    "Joserrili" : "Python"
}

friends = ["José", "Nuria"]
#Accedemos a una posición determinada del diccionario
print("--------------- Posición determinada -------------------------")
print(f"El lenguaje de programación favorito de José es {favorite_languages['José']}.")

#utilizamos el método get() para obtener un valor y que no de error
print("--------------- Método get() para evitar errores -------------")
berta_language = favorite_languages.get("Berta", "No existe lenguaje para Berta")
print(f"El lenguaje de Berta es: {berta_language}.")

ana_language = favorite_languages.get("Ana", "No existe lenguaje para Ana")
print(f"El lenguaje de Ana es: {ana_language}.")

#Recorremos el diccionario para imprimir claves y valores
print("-------------- Diccionario completo --------------------------")
for name, language in favorite_languages.items():
    print(f"El lenguaje favorito de {name.title()} es {language.title()}.")

#Recorremos el diccionario para imprimir claves. Podríamos hacerlo sin .keys()
print("------------- Nombres y lenguaje de los que están en friends -")
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}!")
#Por cada iteración comprobamos si está en la lista friends y si es así 
#imprimimos su lenguaje favorito
    if name in friends:
        print(f"I see you like {favorite_languages[name].title()}.")

#Recorremos el diccionario e imprimimos nombres ordenados alfabéticamente
print("------------ Nombres alfabéticamente ordenados ---------------")
for name in sorted(favorite_languages):
    print(name)

#Recorremos el diccionario para imprimir sólo los valores
print("------------ Imprimimos los lenguajes con values() -----------")
for value in favorite_languages.values():
    print(value)
print("------------ Sin el método values() --------------------------")
for value in favorite_languages:
    print(favorite_languages[value])

#Recorremos el diccionario pero imprimimos sin repeticiones
print("------------ Sin repeticiones con el método values() ---------")
for value in set(favorite_languages.values()):
    print(value)
    
#Conjunto es un tipo de datos que al imprimir no saca los duplicados
#No guarda los datos en un orden específico
print("------------ Creamos un conjunto y lo imprimimos -------------")
conjunto = {"Java", "Python", "Java", "JavaScript"}
print(conjunto)
