from clases.restaurante import Restaurante

class Carrito_helados(Restaurante):
    #Creamos el método init para instanciar el carrito
    def __init__ (self, nombre_restaurante, tipo_cocina):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ['fresa', 'limon', 'plátano', 'naranja', 'chocolate']

    def mostrar_sabores (self):
        print("Los sabores que tenemos son: ")
        for sabor in self.sabores:
            print(f" - {sabor}")