from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='users', null=True, default='others/default_user.png')
    link_web = models.TextField(blank=True, verbose_name='URL de Linkedln')

    def __str__(self):
        return self.user.username