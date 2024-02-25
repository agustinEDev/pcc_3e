class Empleado:
    def __init__(self, nombre, apellido, salario_anual=22000):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_anual = salario_anual

    def dar_aumento(self, aumento = 5000):
        self.salario_anual += aumento

    