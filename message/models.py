from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Message(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = RichTextField(blank=True)
    fecha_mensaje = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario + " - " + self.fecha_mensaje