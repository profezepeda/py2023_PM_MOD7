import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublicacionManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(deleted=False)

class Clasificacion(models.Model):
  nombre = models.CharField(max_length=50, null=False, blank=False)

class Publicacion(models.Model):
  titulo = models.CharField(max_length=200)
  bajada = models.CharField(max_length=200, null=True, blank=True)
  contenido = models.TextField()
  fecha_creacion = models.DateTimeField(default=timezone.now)
  fecha_publicacion = models.DateTimeField(blank=True, null=True)
  autor = models.ForeignKey(User, on_delete=models.PROTECT)
  clasificacion = models.ForeignKey(Clasificacion, on_delete=models.PROTECT, null=True, default=None)
  deleted = models.BooleanField(default=False)

  objects = PublicacionManager()

  def publicar(self):
    self.fecha_publicacion = timezone.now()
    self.save()

  def delete(self, *args, **kwargs):
    self.deleted = True
    self.save()

#class Test(models.Model):
  #id = models.IntegerField(primary_key=True)
  #id = models.CharField(max_length=120, primary_key=True)
  #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#class Test2(models.Model):
  #id_1 = models.IntegerField(null=False)
  #id_2 = models.IntegerField(null=False)
  #nombre = models.CharField(max_length=120, null=False)
  #
  #class Meta:
    #primary_key = ['id_1', 'id_2']