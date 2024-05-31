"""
URL configuration for DreamLeague project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Liga import views as liga_views
from Liga.views import registro, login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", liga_views.Base, name="Base"),
    path("/login", liga_views.login_view, name="login_view"),
    path("/registro", liga_views.registro, name="registro"),
    path("ligas", liga_views.ligas, name="ligas"),
    path("buscar_liga", liga_views.buscar_liga, name="buscar_liga"),
    path("lista_ligas", liga_views.lista_ligas, name="lista_ligas"),
    path("equipos", liga_views.equipos, name="equipos"),
    path("buscar_equipo", liga_views.buscar_equipo, name="buscar_equipo"),
    path("lista_equipos", liga_views.lista_equipos, name="lista_equipos"),
    path("jugadores", liga_views.jugadores, name="jugadores"),
    path("buscar_jugador", liga_views.buscar_jugador, name="buscar_jugador"),
    path("lista_jugadores", liga_views.lista_jugadores, name="lista_jugadores"),
]
