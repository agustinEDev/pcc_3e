from modulos.survey import AnonimousSurvey

#Define una pregunta y hace una encuesta
question = "What language did you first learn to speak?"
language_survey = AnonimousSurvey(question)

#Muestra la pregunta y guarda las respuestas a la pregunta.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#Muestra los resultados de la encuesta.
print("\nThank you to everyone who participated on this survey!")
language_survey.show_results()