class Usuario:

    def __init__(
        #Instanciamos el usuario
            self, 
            username, 
            usr_ap1, usr_ap2, usr_age
            ):
        self.name = username
        self.apellido1 = usr_ap1
        self.apellido2 = usr_ap2
        self.age = usr_age
        self.intentos_inicio = 0

    def describir_usuario (self):
        #Describe el usuario creado con comentarios con sus atributos
        print(f"El usuario se llama {self.name} {self.apellido1} {self.apellido2}.")
        print(f"La edad del usuario es {self.age}.")
        print(f"El número de reintentos es {self.intentos_inicio}")

    def saludar_usuario (self):
        #Saluda al usuario recibido
        nombre = f'{self.name} {self.apellido1} {self.apellido2}'
        print(f"Hola, {nombre}!")

    def incrementar_intentos_inicio (self):
        #Incrementa el número de intentos de inicio de sesión
        self.intentos_inicio += 1

    def restablecer_intentos_inicio (self):
        #Restablece el número de inicios de sesión
        self.intentos_inicio = 0