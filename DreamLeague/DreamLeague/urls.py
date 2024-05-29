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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", liga_views.Base, name="Base"),
    path("login", liga_views.login, name="login"),
    path("registro", liga_views.registro, name="registro"),
    path("ligas", liga_views.ligas, name="ligas"),
    path("equipos", liga_views.equipos, name="equipos"),
    path("jugadores", liga_views.jugadores, name="jugadores"),
]
