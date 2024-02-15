from django.forms import ModelForm
from .models import Blog
from django.forms import TextInput, FileInput, Textarea

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),
            'subtitulo': TextInput(attrs={'class': 'form-control'})
        }