import pytest
from survey import AnonimousSurvey

@pytest.fixture
def language_survey():
    #Una encuesta disponible para todas las funciones de la prueba
    question = "What language did you first learn to speak?"
    language_survey = AnonimousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    #Comprobar que una respuesta única se almacena correctamente
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    #Comprueba que se guardan correctamente 3 respuestas
    responses = ['English', 'Mandarin', 'Spanish']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses