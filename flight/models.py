from django.db import models

# Create your models here.


class Flight(models.Model): 
    TIPO_CHOICES = [
        ('NACIONAL', 'Nacional'),
        ('INTERNACIONAL', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.nombre} - {self.tipo} (${self.precio})"
