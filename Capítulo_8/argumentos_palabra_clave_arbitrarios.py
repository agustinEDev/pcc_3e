#Indicamos que vamos a recibir argumentos de palabra clave arbitrarios
#Recibe un nombre, un apellido y uno o más argumentos de palabra clave
def buid_profile (first, last, **user_info):
    user_info['First name'] = first
    user_info['Last name'] = last
    return user_info

info = buid_profile('Albert', 'Einstein', location = 'Princeton', area = 'Physics')
print(info)