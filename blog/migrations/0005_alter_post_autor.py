# Generated by Django 5.1.6 on 2025-03-07 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_fecha_publicacion_post_imagen_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor'),
        ),
    ]
