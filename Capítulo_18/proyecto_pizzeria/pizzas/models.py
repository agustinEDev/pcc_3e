from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pizza (models.Model):
    """Una pizza que el usuario puede pedir."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(default  = timezone.now)

    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.name
    
class Ingrediente (models.Model):
    """Ingredientes para las pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default  = timezone.now)

    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.name