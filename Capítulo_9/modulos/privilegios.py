class Privilegios():

    def __init__ (self):
        #Crea una instancia de la clase Privilegios
        self.privilegios = [
            "Puede editar ficheros",
            "Puede eliminar ficheros",
            "Puede crear nuevos usuarios"
        ]

    def show_privileges (self):
        #Imprime por pantalla los privilegios de la instancia
        print("Privilegios de usuario Admin: ")
        for privilege in self.privilegios:
            print(f" - {privilege.title()}")