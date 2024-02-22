class Battery:

    def __init__(self, battery_size = 40):
        #Inicializamos los atributos de la batería
        self.battery_size = battery_size

    def describe_battery (self):
        #Describe el tamaño de la batería
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range (self):
        #Imprimimos información sobre la autonomía de la batería
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            print("We have no range for this battery size.")
            range = 0
        
        if range != 0:
            print(f"This car can go about {range} miles on a full charge.")