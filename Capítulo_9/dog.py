class Dog:
    """Un intento sencillo de modelar un perro."""

    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula un perro sentándose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula un perro haciendo la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")

my_dog = Dog("Ton", 12)
print(f"My dog´s name is {my_dog.name}.")
print(f"My dog´s {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Moncha", 8)
print(f"Your dog´s name is {your_dog.name}.")
print(f"Your dog´s {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
