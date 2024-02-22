import sys
sys.path.append("../clases/")
from clases.usuario import Usuario
from clases.admin import Admin

user1 = Usuario("Agustín", "Estévez", "Domínguez", 43)
user2 = Usuario("Emma", "Domínguez", "Pedrosa", 81)
user3 = Usuario("Carmen", "Estévez", "Domínguez", 41)
user4 = Admin("José", "Viqueira", "Moreu", 5)

user1.incrementar_intentos_inicio()
user1.incrementar_intentos_inicio()
user1.incrementar_intentos_inicio()

user1.describir_usuario()
user1.saludar_usuario()
user1.restablecer_intentos_inicio()
user1.describir_usuario()
print("\n")

user2.describir_usuario()
user2.saludar_usuario()
print("\n")

user3.describir_usuario()
user3.saludar_usuario()
print("\n")

user4.describir_usuario()
user4.saludar_usuario()
user4.privilegios.show_privileges()
print("\n")