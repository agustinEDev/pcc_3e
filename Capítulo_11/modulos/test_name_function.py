from name_function import get_formated_name

def test_first_last_name():
    #Funcionan nombres como Janis Joplin?
    formatted_name = get_formated_name('Janis', 'Joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    #Funcionan nombres como Wolfgang Amadeus Mozart?
    formatted_name = get_formated_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'

#Para ejecutar la prueba, tenemos que escribir python3 -m pytest