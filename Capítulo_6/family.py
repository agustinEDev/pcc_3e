#Inicializamos un diccionario
miembros = int(input("\nCuántos miembros tiene su familia? "))
familia = []
#Creamos tantos diccionarios como miembros tiene la familia
#Los añadimos a la lisra familia[]
for number in range(miembros):
    new_miembro = {'número' : number + 1, 'nombre' : '', 'apellido1' : '', 'apellido2' : '', 'edad' : 0}
    familia.append(new_miembro)
print("\n")
#Recorremos la lista pidiendo los datos de los miembros si no existen
for miembro in familia:
    if miembro['nombre'] == '':
        miembro['nombre'] = input(f"Introduzca el nombre del miembro número {miembro['número']}: ")
    else:
        print(f"El nombre es {miembro['nombre']}.")

    if miembro['apellido1'] == '':
        miembro['apellido1'] = input(f"Introduzca el primer apellido del miembro número {miembro['número']}: ")
    else:
        print(f"El primer apellido es {miembro['apellido1']}.")

    if miembro['apellido2'] == '':
        miembro['apellido2'] = input(f"Introduzca el segundo apellido del miembro número {miembro['número']}: ")
    else:
        print(f"El segundo apellido es {miembro['apellido2']}.")

    if miembro['edad'] == 0:
        miembro['edad'] = input(f"Introduzca la edad del miembro número {miembro['número']}: ")
    else:
        print(f"La edad es {miembro['edad']}.")
    print("Miembro almacenado.\n")

#Preguntamos si quieren verse los datos introducidos
pregunta = input("\nQuiere ver los datos familiares? (si/no) ")
if pregunta == 'si':
    for miembro in familia:
        nombre_completo = f"{miembro['nombre']} {miembro['apellido1']} {miembro['apellido2']}"
        print(f"El nombre del {miembro['número']} miembro de la familia es {nombre_completo.title()} y tiene {miembro['edad']} años.")
else:
    print('\n')

print("Fin del programa.")


