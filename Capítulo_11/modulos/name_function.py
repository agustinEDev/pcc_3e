def get_formated_name (first, last, middle=''):
    #Genera un nombre completo con formato adecuado.
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title().strip()