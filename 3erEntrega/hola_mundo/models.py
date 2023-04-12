from django.db import models

class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    cantidad = models.IntegerField()
    id_Producto = models.IntegerField()
    def __str__(self):
        return f" {self.id} - {self.id_Producto} - {self.nombre}"


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f" {self.id} - {self.nombre} - {self.apellido}"
    
class Venta(models.Model):
    nombre = models.TextField(max_length=100)
    cantidad = models.TextField(max_length=100)
    condicion = models.TextField(max_length=100)
    id_Producto = models.IntegerField()
    
    def __str__(self):
        return f" {self.id} - {self.nombre} - {self.cantidad} - {self.condicion} - {self.id_Producto}"


