# Generated by Django 5.0.2 on 2024-02-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(default='others/default_blog.png', null=True, upload_to='blogs'),
        ),
    ]
