from modulos.usuario import Usuario
from modulos.privilegios import Privilegios

class Admin(Usuario):

    def __init__(
        #Instanciamos el usuario admin
            self, 
            username, 
            usr_ap1, usr_ap2, usr_age
            ):
        super().__init__(username, 
            usr_ap1, usr_ap2, usr_age
        )
        self.privilegios = Privilegios()

