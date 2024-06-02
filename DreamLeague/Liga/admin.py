from django.contrib import admin
from .models import Liga, Equipo, Jugador, Avatar

admin.site.register(Liga)
admin.site.register(Equipo)
admin.site.register(Jugador)


class AvatarAdmin(admin.ModelAdmin):
    model = Avatar
    list_display = ("user", "image")


admin.site.register(Avatar, AvatarAdmin)
