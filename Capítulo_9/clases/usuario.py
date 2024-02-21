class Usuario:

    def __init__(
            self, 
            username, 
            usr_ap1, usr_ap2, usr_age
            ):
        self.name = username
        self.apellido1 = usr_ap1
        self.apellido2 = usr_ap2
        self.age = usr_age

    def describir_usuario (self):
        print(f"El usuario se llama {self.name} {self.apellido1} {self.apellido2}.")
        print(f"La edad del usuario es {self.age}.")

    def saludar_usuario (self):
        nombre = f'{self.name} {self.apellido1} {self.apellido2}'
        print(f"Hola, {nombre}!")