# Generated by Django 4.2.3 on 2023-07-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categorias',
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
    ]
