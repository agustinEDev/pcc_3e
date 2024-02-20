import os

#Esta es la función que pregunta si continuamos o no con la aplicación
def continuar():
    repeat = input("Do you want to continue? yes/no: ")
    while repeat not in ('yes','no'):
        print("It is not a valid answer.")
        repeat = input("Do you want to continue? yes/no: ")
    
    if repeat == 'yes':
        return True
    else:
        return False
    
#Almacenar discos
def almacenar_discos(discos):
        
        nom_ar = input("Introduzca el nombre del artista: ")
        nom_dis = input("Introduzca el nombre del album: ")
        canciones = input ("Quiere introducir el número de canciones? (si/no): ")
        while canciones.lower() not in ('si', 'no'):
            print(f"'{canciones}' no es una opción correcta.")
            canciones = input ("Quiere introducir el número de canciones? (si/no): ")

        if canciones == 'no':
            discos.append(hacer_album(nom_ar, nom_dis))
        else:
            num_canc = input("Introduzca el número de canciones del álbum: ")
            discos.append(hacer_album(nom_ar, nom_dis, num_canc))
        return discos
    
#Hacer disco
def hacer_album (artista, album, num_canciones = 'none'):

    if num_canciones != 'none':
        num_canciones = int(num_canciones)

    album = {
        'Artista' : artista,
        'Álbum' : album,
        'Número de canciones' : num_canciones
    }

    return album

#Mostrar discos
def mostrar_discos(discos):
    if discos == []:
        print("No hay discos guardados.")
    else:
        print("Listado de discos: ")
        for disco in discos:
            print("Álbum -----------")
            for key, value in disco.items():
                if value != 'none':
                    print(f"{key.title()}: {value}")
    input("Pulse enter.")

#Menú principal
def menu_principal():
    opt = 0

    while opt not in (1, 2, 3):
        print("------- Menú principal -------")
        print("1. Almacenar disco.")
        print("2. Ver discos almacenados")
        print("3. Salir.")
        opt = int(input("Qué desea hacer?: "))

        if opt not in (1, 2, 3):
            print("Opción incorrecta. Pulse enter.")
            input()
            os.system("clear")
    return opt


# -------------------- Inicio del programa ------------------------------------
os.system('clear')
print("Bienvenido al almacén de discos.")
flag = True
discos = []
option = 0

while flag:
    if option != 0:
        os.system("clear")
    option = menu_principal()

    if option == 1:
        os.system("clear")
        discos = almacenar_discos(discos)
        continue
    elif option == 2:
        os.system("clear")
        mostrar_discos(discos)
        continue
    else:
        os.system("clear")
        flag = False


