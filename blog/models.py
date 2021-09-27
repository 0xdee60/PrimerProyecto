from django.db import models
from django.db.models.base import Model

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()

    def __str__(self) -> str:
        return self.titulo

