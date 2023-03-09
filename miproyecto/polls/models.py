from django.db import models

# Create your models here.
class pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicación')

    def __str__(self):
        return self.texto_pregunta
    
class Eleccion(models.Model):
    pregunta_fk=models.ForeignKey(pregunta, on_delete=models.CASCADE)
    texto_eleccion=models.CharField(max_length=200)
    votos=models.IntegerField(default=0)

    def __str__(self):
        return self.pregunta_fk.texto_pregunta + ' '+ self.texto_eleccion
