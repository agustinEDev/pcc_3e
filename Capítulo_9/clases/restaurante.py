class Restaurante:

    #Método init
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre = nombre_restaurante
        self.tipo = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre.title()}.")
        print(f"El tipo de cocina es {self.tipo}.")

    def abrir_restaurante(self):
        print("El restaurante está abierto.")

    def cerrar_restaurante(self):
        print("El restaurante está cerrado.")