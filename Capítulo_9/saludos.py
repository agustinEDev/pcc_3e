import sys
sys.path.append("../clases/")
import clases.usuario as usuario

user1 = usuario.Usuario("Agustín", "Estévez", "Domínguez", 43)
user2 = usuario.Usuario("Emma", "Domínguez", "Pedrosa", 81)
user3 = usuario.Usuario("Carmen", "Estévez", "Domínguez", 41)

user1.describir_usuario()
user1.saludar_usuario()
print("\n")

user2.describir_usuario()
user2.saludar_usuario()
print("\n")

user3.describir_usuario()
user3.saludar_usuario()
print("\n")