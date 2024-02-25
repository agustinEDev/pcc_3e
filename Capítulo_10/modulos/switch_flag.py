def set_flag_en():
    #This is the function which asks if the app continues or not
    repeat = input("Do you want to continue? yes/no: ")
    while repeat.lower() not in ('yes','no'):
        print("It is not a valid answer.")
        repeat = input("Do you want to continue? yes/no: ")
    
    if repeat.lower() == 'yes':
        return True
    else:
        return False

def set_flag_es():
    #Esta es la función que pregunta si continuamos o no con la aplicación
    repeat = input("Quieres continuar? (si/no): ")
    while repeat.lower() not in ('si','no'):
        print("No es una respuesta válida.")
        repeat = input("Quieres continuar? (si/no): ")
    
    if repeat.lower() == 'si':
        return True
    else:
        return False