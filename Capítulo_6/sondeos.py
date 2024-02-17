#Inicializamos un diccionario
favorite_languages = {
    "Agustín" : "Python",
    "José" : "C#",
    "Nuria" : "Java",
    "Ana" : "HTML",
    "Joserrili" : "Python"
}

#Inicializamos una lista
muestreo = ["Juan", "Pedro", "Carlos", "Nuria", "Francisco", "Agustín"]

for name in muestreo:
    if name in favorite_languages.keys():
        print(f"Gracias por haber participado en nuestra encuesta, {name.title()}.")
    else:
        print(f"No te olvides de participar en nuestra encuesta, {name.title()}.")