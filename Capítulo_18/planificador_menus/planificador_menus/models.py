from django.db import models

class Dia_Semana(models.Model):
    nombre = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'dias_semana'
    
    def __str__(self):
        return self.nombre
    
class Plato(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Entrada(models.Model):
    nombre = models.CharField(max_length=50)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    dia_semana = models.ForeignKey(Dia_Semana, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
