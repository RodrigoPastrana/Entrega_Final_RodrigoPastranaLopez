# Generated by Django 5.0.6 on 2024-06-04 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0003_alter_avatar_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='division',
            new_name='liga',
        ),
    ]
