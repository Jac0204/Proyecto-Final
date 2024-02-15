from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    """ cuerpo = models.TextField(blank=True) """
    cuerpo = RichTextField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blogs', null=True, default='others/default_blog.png')

    def __str__(self):
        return self.titulo + " - Creador por: " + self.autor.username