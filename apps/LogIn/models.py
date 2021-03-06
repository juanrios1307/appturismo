from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaNacimiento=models.DateTimeField(auto_now_add=True, auto_now=False)
    email = models.EmailField()
    telefono= models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email
