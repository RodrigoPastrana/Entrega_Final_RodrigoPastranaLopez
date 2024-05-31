from django.shortcuts import render, redirect
from .forms import LigaForm, EquipoForm, JugadorForm, LigaSearchForm
from .models import Liga, Equipo, Jugador
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


def Base(request):
    return render(request, "Liga/Base.html")


def ligas(request):
    if request.method == "POST":
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = LigaForm()
    return render(request, "Liga/ligas.html", {"form": form})


def buscar_liga(request):
    form = LigaSearchForm()
    resultados = None
    if "query" in request.GET:
        form = LigaSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Liga.objects.filter(nombre__icontains=query)
    return render(request, "Liga/buscar_liga.html", {"form": form, "resultados": resultados})


def lista_ligas(request):
    return render(request, "Liga/lista_ligas.html")


def equipos(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = EquipoForm()
    return render(request, "Liga/equipos.html", {"form": form})


def buscar_equipo(request):
    return render(request, "Liga/buscar_equipo.html")


def lista_equipos(request):
    return render(request, "Liga/lista_equipos.html")


def jugadores(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = JugadorForm()
    return render(request, "Liga/jugadores.html", {"form": form})


def buscar_jugador(request):
    return render(request, "Liga/buscar_jugador.html")


def lista_jugadores(request):
    return render(request, "Liga/lista_jugadores.html")


def registro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("Base")
    else:
        form = RegisterForm()
    return render(request, "Liga/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Base")
    else:
        form = AuthenticationForm()
    return render(request, "Liga/login.html", {"form": form})
