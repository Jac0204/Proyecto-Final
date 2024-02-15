from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = (
        'fecha_creacion',
        'id',
    )

admin.site.register(Blog, BlogAdmin)