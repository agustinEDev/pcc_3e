def imprimir_mensajes (mensajes):
    while mensajes:
        mensaje_actual = mensajes.pop()
        print(f"{mensaje_actual}")
    print(f"Lista: {mensajes}") 

mensajes = ['Carpe diem!', 'Viva la vida!', 'La vida es maravillosa!', 'All you need is love!']
#Enviamos una copia de la lista, así no perdemos los datos
auxiliar = imprimir_mensajes(mensajes[:])
print(f"Principal: {mensajes}")