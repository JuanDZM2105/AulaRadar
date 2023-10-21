from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class universidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50000)
    ubicacion = models.CharField(max_length=50)
    

