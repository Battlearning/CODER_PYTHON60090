from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre del curso:  {self.nombre} -- Número de Comisión: {self.camada}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    email = models.EmailField ()

    def __str__(self):
        return f"Alumno:  {self.nombre} {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) 
    email = models.EmailField ()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"Profesor:  {self.nombre} {self.apellido}, {self.profesion}"
    
     
class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechadeentrega = models.DateField() 
    entregado = models.BooleanField()

    def __str__(self):
        return f"Entrega:  {self.nombre}, estado:  {self.entregado}"