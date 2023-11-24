from django.contrib.auth.models import User
from django.db import models

TIPO_OPCIONES = [
        ('publico', 'Público'),
        ('privado', 'Privado'),
    ]

class universidad(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    ubicacion = models.CharField(max_length=50)
    id_unico = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to='mainRadar1/imagenes', null=True)
     

    tipo = models.CharField(max_length=10, choices=TIPO_OPCIONES, default='publico')
    
    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    id_usuario = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.nombre

class programa_academicos(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    id_unico  = models.IntegerField(primary_key=True)
    id_universidad = models.ForeignKey(universidad, on_delete=models.CASCADE)
    precio_medio = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.nombre
    
class curso(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    precio =models.FloatField()
    id_unico2 = models.IntegerField(primary_key=True)
    id_universidad = models.ForeignKey(universidad,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    

class curso_programa(models.Model):
    
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_programa_academico = models.ForeignKey(programa_academicos, on_delete=models.CASCADE)
    id_unico4 = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.id_curso.nombre
    
class comentario(models.Model):
    
    id_curso = models.ForeignKey(curso,null=True, on_delete=models.CASCADE)
    id_programa_academico = models.ForeignKey(programa_academicos,null=True, on_delete=models.CASCADE)
    id_universidad = models.ForeignKey(universidad,null=True,  on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=2000)
    id_unico3 = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        len_title = 15
        if len(self.descripcion) > len_title:
            titlestring = self.descripcion[:len_title] + '...'
        return self.descripcion