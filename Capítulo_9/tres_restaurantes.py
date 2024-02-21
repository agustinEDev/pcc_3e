import sys
sys.path.append('../clases/')
import clases.restaurante as restaurante



furancho = restaurante.Restaurante("Las Torres", "Mediterránea")
furancho2 = restaurante.Restaurante("La Ostra Azul", "Fusión")
furancho3 = restaurante.Restaurante("El Bulli", "Brasa")

furancho.describir_restaurante()
furancho2.describir_restaurante()
furancho3.describir_restaurante()