from django.db import models
from django.contrib.auth.models import User


class Liga(models.Model):
    nombre = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = (
            "nombre",
            "usuario",
        )

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = (
            "nombre",
            "usuario",
        )

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = (
            "nombre",
            "usuario",
        )

    def __str__(self):
        return self.nombre


class Avatar(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatares")
