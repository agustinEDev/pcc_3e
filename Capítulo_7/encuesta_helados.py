import os
#Inicializamos el diccionario
respuestas = {}

#Configuramos un flag para indicar que la encuesta está activa
flag = True
os.system('clear')
while flag:
    #Pedimos el nombre y la respuesta
    name = input('Introduce tu nombre: ')
    response = input('Cuál es tu helado favorito? ')

    #Guardamos la respuesta en el diccionario
    respuestas[name] = response

    #Preguntamos si va a haber más respuestas
    repeat = input("Quieres seguir con la encuesta? (si/no) ")
    while repeat not in ('si', 'no'):
        print("No es una respuesta válida.")
        repeat = input("Quieres seguir con la encuesta? (si/no) ")

    if repeat == 'no':
        flag = False

#La encuesta está finalizada, enseñamos los resultados
print("\n------------ Resultados de la encuesta ------------")
for name, response in respuestas.items():
    print(f"El helado favorito de {name.title()} es el de {response}.")