# Generated by Django 5.0.6 on 2024-06-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0002_alter_jugador_equipo_alter_jugador_nombre_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(upload_to='avatares'),
        ),
    ]