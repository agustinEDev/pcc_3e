#Inicializamos un diccionario anidado
usuarios = {
    'josevg' : {
        'nombre' : 'josé',
        'apellido1' : 'viqueira',
        'apellido2' : 'garcía',
        'ubicación' : 'vigo'
    },
    'agustined' : {
        'nombre' : 'agustín',
        'apellido1' : 'estévez',
        'apellido2' : 'domínguez',
        'ubicación' : 'pontevedra'
    }
}

for username, userinfo in usuarios.items():
    print(f"\nNombre de usuario: {username}")
    nombre_completo = f"{userinfo['nombre'].title()} {userinfo['apellido1'].title()} {userinfo['apellido2'].title()}"

    print(f"\tNombre completo: {nombre_completo}")
    print(f"\tLocalización: {userinfo['ubicación'].title()}")