from django.shortcuts import render, redirect
#from .forms import DivisiónForm, EquipoForm, JugadorForm, DivisionSearchForm
#from .models import División, Equipo, Jugador


def Base(request):
    return render(request, "Liga/Base.html")
