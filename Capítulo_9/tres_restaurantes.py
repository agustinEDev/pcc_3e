import sys
sys.path.append('../clases/')
from clases.restaurante import Restaurante
from clases.carrito_helados import Carrito_helados


furancho = Restaurante("Las Torres", "Mediterránea")
furancho2 = Restaurante("La Ostra Azul", "Fusión")
furancho3 = Restaurante("El Bulli", "Brasa")
my_carrito = Carrito_helados("Helados Paco", "Heladería")

furancho.establecer_numero_servido(35)
furancho2.incrementar_numero_servido(5)
furancho3.incrementar_numero_servido(12)

furancho.describir_restaurante()
furancho2.describir_restaurante()
furancho3.describir_restaurante()
my_carrito.establecer_numero_servido(134)
my_carrito.describir_restaurante()
my_carrito.mostrar_sabores()