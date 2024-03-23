from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Una pizza que el usuario puede pedir."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.name
    
class Ingrediente (models.Model):
    """Ingredientes para las pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.name