# Generated by Django 5.1.6 on 2025-03-06 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_autor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
    ]
