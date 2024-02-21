import sys
sys.path.append("../clases/")
from clases.car import Car 

class ElectricCar (Car):

    def __init__(self, make, model, year):
        #Inicializa los atributos de la clase base
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_batery (self):
        #Describe el tamaño de la batería
        print(f"This car has a {self.battery_size}-kWh battery.")