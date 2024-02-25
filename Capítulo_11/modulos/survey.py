class AnonimousSurvey:
    #Recoge respuestas anónimas a una pregunta de una encuesta

    def __init__(self, question):
        #Guarda una pregunta y se prepara para guardar respuestas
        self.question = question
        self.responses = []

    def show_question(self):
        #Muestra la pregunta del sondeo
        print (self.question)

    def store_response(self, new_response):
        #Guarda una sola respuesta a la encuesta
        self.responses.append(new_response)

    def show_results(self):
        #Muestra todas las respuestas que se han dado.
        print("Survey results: ")
        for response in self.responses:
            print(f" - {response}")