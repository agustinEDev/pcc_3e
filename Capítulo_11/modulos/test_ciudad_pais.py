from city_country import devolver_city_country

def test_get_city_coutry ():
    #Funcionará la función para Santiago y Chile?
    texto_formateado = devolver_city_country('santiago', 'chile', 5000000)
    assert texto_formateado == 'Santiago, Chile - habitantes 5000000'