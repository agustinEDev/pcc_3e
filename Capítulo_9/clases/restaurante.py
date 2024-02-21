class Restaurante:

    #Método init
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante
        self.tipo = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre.title()}.")
        print(f"El tipo de cocina es {self.tipo}.")
        print(f"El restaurante ha servido a {self.numero_servido} clientes.")

    def abrir_restaurante(self):
        print("El restaurante está abierto.")

    def cerrar_restaurante(self):
        print("El restaurante está cerrado.")

    def establecer_numero_servido (self, servidos):
        if self.numero_servido <= servidos:
            self.numero_servido = servidos
        else:
            print("No se puede reducir el número de clientes servidos.")

    def incrementar_numero_servido (self, servidos):
        if servidos >= 0:
            self.numero_servido += servidos
        else:
            print("No se puede disminuir el número de clientes servidos.")