def devolver_city_country (city, country, population=''):
    #Devuelve la ciudad y el país formateado
    if population:
        return f'{city.title()}, {country.title()} - habitantes {population}'
    else:
        return f'{city.title()}, {country.title()}'