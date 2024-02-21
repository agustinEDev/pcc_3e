import sys
sys.path.append('../clases/')
from clases.restaurante import Restaurante


furancho = Restaurante("Las Torres", "Mediterránea")
furancho2 = Restaurante("La Ostra Azul", "Fusión")
furancho3 = Restaurante("El Bulli", "Brasa")

furancho.establecer_numero_servido(35)
furancho2.incrementar_numero_servido(5)
furancho3.incrementar_numero_servido(12)

furancho.describir_restaurante()
furancho2.describir_restaurante()
furancho3.describir_restaurante()