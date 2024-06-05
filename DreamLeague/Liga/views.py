from django.shortcuts import render, redirect, get_object_or_404
from .forms import LigaForm, EquipoForm, JugadorForm, LigaSearchForm
from .models import Liga, Equipo, Jugador
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def Base(request):
    return render(request, "Liga/Base.html")


def sobre_mi(request):
    return render(request, "Liga/sobre_mi.html")


@login_required
def ligas(request):
    if request.method == "POST":
        form = LigaForm(request.POST)
        if form.is_valid():
            liga = form.save(commit=False)
            liga.usuario = request.user
            liga.save()
            return redirect("Base")
    else:
        form = LigaForm()
    return render(request, "Liga/ligas.html", {"form": form})


@login_required
def buscar_liga(request):
    form = LigaSearchForm()
    resultados = None
    if "query" in request.GET:
        form = LigaSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Liga.objects.filter(nombre__icontains=query, usuario=request.user)
    return render(request, "Liga/buscar_liga.html", {"form": form, "resultados": resultados})


@login_required
def lista_ligas(request):
    ligas = Liga.objects.filter(usuario=request.user)
    return render(request, "Liga/lista_ligas.html", {"ligas": ligas})


@login_required
def detalle_liga(request, pk):
    liga = get_object_or_404(Liga, pk=pk, usuario=request.user)
    return render(request, "Liga/detalle_liga.html", {"liga": liga})


@login_required
def editar_liga(request, pk):
    liga = get_object_or_404(Liga, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = LigaForm(request.POST, instance=liga)
        if form.is_valid():
            form.save()
            return redirect("lista_ligas")
    else:
        form = LigaForm(instance=liga)
    return render(request, "Liga/editar_liga.html", {"form": form})


@login_required
def eliminar_liga(request, pk):
    liga = get_object_or_404(Liga, pk=pk, usuario=request.user)
    if request.method == "POST":
        liga.delete()
        return redirect("lista_ligas")
    return render(request, "Liga/confirmar_eliminacion.html", {"obj": liga})


@login_required
def equipos(request):
    if request.method == "POST":
        form = EquipoForm(request.POST, user=request.user)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.usuario = request.user
            equipo.save()
            return redirect("Base")
    else:
        form = EquipoForm(user=request.user)
        ligas = Liga.objects.filter(usuario=request.user)
    return render(request, "Liga/equipos.html", {"form": form, "ligas": ligas})


@login_required
def buscar_equipo(request):
    query = request.GET.get("q")
    equipos = []
    if query:
        equipos = Equipo.objects.filter(nombre__icontains=query, usuario=request.user)
    return render(request, "Liga/buscar_equipo.html", {"equipos": equipos, "query": query})


@login_required
def lista_equipos(request):
    equipos = Equipo.objects.filter(usuario=request.user)
    return render(request, "Liga/lista_equipos.html", {"equipos": equipos})


@login_required
def detalle_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk, usuario=request.user)
    return render(request, "Liga/detalle_equipo.html", {"equipo": equipo})


@login_required
def editar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("lista_equipos")
    else:
        form = EquipoForm(instance=equipo, user=request.user)
        form.fields["liga"].widget.attrs.update({"class": "form-control edit-specific-class"})
    return render(request, "Liga/editar_equipo.html", {"form": form})


@login_required
def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk, usuario=request.user)
    if request.method == "POST":
        equipo.delete()
        return redirect("lista_equipos")
    return render(request, "Liga/confirmar_eliminacion.html", {"obj": equipo})


@login_required
def jugadores(request):
    if request.method == "POST":
        form = JugadorForm(request.POST, user=request.user)
        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.usuario = request.user
            jugador.save()
            return redirect("Base")
    else:
        form = JugadorForm(user=request.user)
    return render(request, "Liga/jugadores.html", {"form": form})


@login_required
def buscar_jugador(request):
    query = request.GET.get("query", "")
    jugadores = []
    if query:
        jugadores = Jugador.objects.filter(nombre__icontains=query, usuario=request.user)
    return render(request, "Liga/buscar_jugador.html", {"jugadores": jugadores})


@login_required
def lista_jugadores(request):
    jugadores = Jugador.objects.filter(usuario=request.user)
    return render(request, "Liga/lista_jugadores.html", {"jugadores": jugadores})


@login_required
def detalle_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk, usuario=request.user)
    return render(request, "Liga/detalle_jugador.html", {"jugador": jugador})


@login_required
def editar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = JugadorForm(request.POST, instance=jugador, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("lista_jugadores")
    else:
        form = JugadorForm(instance=jugador, user=request.user)
        form.fields["equipo"].widget.attrs.update({"class": "form-control edit-specific-class"})
    return render(request, "Liga/editar_jugador.html", {"form": form})


@login_required
def eliminar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk, usuario=request.user)
    if request.method == "POST":
        jugador.delete()
        return redirect("lista_jugadores")
    return render(request, "Liga/confirmar_eliminacion.html", {"obj": jugador})


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
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Base")
    else:
        form = CustomAuthenticationForm()
    return render(request, "Liga/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("Base")


def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("Base")
    else:
        message = "Es necesario iniciar sesión para crear ligas, equipos o jugadores."
        context = {"message": message}
        return LoginView.as_view(template_name="Liga/login.html", extra_context=context)(request, *args, **kwargs)
