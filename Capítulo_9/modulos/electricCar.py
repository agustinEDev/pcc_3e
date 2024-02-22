from modulos.car import Car 
from modulos.battery import Battery

class ElectricCar (Car):

    def __init__(self, make, model, year):
        #Inicializa los atributos de la clase base
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        #El coche electrico no tiene depósito
        print("Electric cars has no gas tank.")