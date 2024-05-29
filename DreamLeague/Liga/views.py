from django.shortcuts import render, redirect
from .forms import LigaForm, EquipoForm, JugadorForm, LigaSearchForm
from .models import Liga, Equipo, Jugador


def Base(request):
    return render(request, "Liga/Base.html")


def login(request):
    return render(request, "Liga/login.html")


def registro(request):
    return render(request, "Liga/registro.html")


def ligas(request):
    if request.method == "POST":
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = LigaForm()
    return render(request, "Liga/ligas.html", {"form": form})


def equipos(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = EquipoForm()
    return render(request, "Liga/equipos.html", {"form": form})


def jugadores(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = JugadorForm()
    return render(request, "Liga/jugadores.html", {"form": form})


def buscar_division(request):
    form = LigaSearchForm()
    resultados = None
    if "query" in request.GET:
        form = LigaSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Liga.objects.filter(nombre__icontains=query)
    return render(request, "Liga/buscar_division.html", {"form": form, "resultados": resultados})
