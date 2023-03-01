from django.db import models

# Create your models here.
class pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicación')

    def __str__(self):
        return self.texto_pregunta
