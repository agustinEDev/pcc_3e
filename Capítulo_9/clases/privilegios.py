class Privilegios():

    def __init__ (self):
        self.privilegios = [
            "Puede editar ficheros",
            "Puede eliminar ficheros",
            "Puede crear nuevos usuarios"
        ]

    def show_privileges (self):
        print("Privilegios de usuario Admin: ")
        for privilege in self.privilegios:
            print(f" - {privilege.title()}")