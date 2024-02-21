class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name (self):
        #Devuelve un nombre descriptivo con el formato correcto
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer (self):
        #Imprime una oración que indica el kilometraje del automóvil
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer (self, mileage):
        #Actualiza el valor del kilometraje siempre que sea mayor al actual
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can´t roll back an odometer.")

    def increment_odometer (self, mileages):
        #Incrementa el kilometraje con la cantidad recibida
        if mileages >= 0:
            self.odometer_reading += mileages