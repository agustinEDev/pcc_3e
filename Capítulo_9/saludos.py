import sys
sys.path.append("../clases/")
from clases.usuario import Usuario

user1 = Usuario("Agustín", "Estévez", "Domínguez", 43)
user2 = Usuario("Emma", "Domínguez", "Pedrosa", 81)
user3 = Usuario("Carmen", "Estévez", "Domínguez", 41)

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