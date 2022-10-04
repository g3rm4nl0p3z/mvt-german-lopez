from django.db import models

"""
    MODELO PERSONA (atributos):
        - Nombre: str
        - Apellido: str
        - Edad: int
        - Email: str
        - Fecha carga: datetime
"""
class Persona(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    email = models.EmailField(max_length=100)

    fecha_carga = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Persona: {self.nombre} {self.apellido}. Edad {self.edad}. Correo {self.email}'
