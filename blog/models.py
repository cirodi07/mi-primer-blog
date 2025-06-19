from django.conf import settings
from django.db import models
from django.utils import timezone
#python manage.py makemigrations blog => para craer los modelos
#python manage.py migrate blog
class Publicacion(models.Model):
  autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  titulo = models.CharField(max_length=200)
  texto = models.TextField()
  fecha_creacion = models.DateTimeField(default=timezone.now)
  fecha_publicacion = models.DateTimeField(blank=True, null=True)
  def publicar(self):
    self.fecha_publicacion = timezone.now()
    self.save()
  def __str__(self):
    return self.titulo

class Astro(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.TextField()
  diametro = models.FloatField()
  masa = models.CharField(max_length=100)
  distancia_sol = models.FloatField(null=True, blank=True)
  periodo_dias = models.FloatField(null=True, blank=True)
  periodo_años = models.FloatField(null=True, blank=True)
  lunas = models.FloatField(null=True, blank=True)
  escala = models.FloatField()
  rotacion = models.FloatField()
  imagen = models.ImageField(upload_to='astros/')
  fecha_creacion = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.nombre