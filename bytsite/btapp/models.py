from django.db import models
from django.utils import timezone

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
        
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('auth.User')
    texto = models.TextField()
    imagen = models.ImageField(upload_to='images/data',blank=True,null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    destacado = models.BooleanField(default='false')
    def __str__(self):
        return self.titulo
        
class Banner(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/data',blank=True,null=False)
    orden_banner = models.IntegerField(default=0)
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=8)
    empresa  = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='images/data',blank=True,null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/data',blank=True,null=False)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_cliente
    
        