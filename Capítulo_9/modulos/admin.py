from clases.usuario import Usuario
from clases.privilegios import Privilegios

class Admin(Usuario):

    def __init__(
            self, 
            username, 
            usr_ap1, usr_ap2, usr_age
            ):
        super().__init__(username, 
            usr_ap1, usr_ap2, usr_age
        )
        self.privilegios = Privilegios()

