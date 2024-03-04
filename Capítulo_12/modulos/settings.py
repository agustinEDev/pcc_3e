class Settings:
    #Clase para guardar toda la configuración de Aline Invasion.

    def __init__ (self):
        #Inicializa la configuración del juego.
        #Configuración de la pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 10

        #Configuración de la nave
        self.gargola_speed = 5.0

        #Configuración de las balas
        self.bullet_speed = 4.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        #configuracion de los aliens
        self.pixel_speed = 0.5