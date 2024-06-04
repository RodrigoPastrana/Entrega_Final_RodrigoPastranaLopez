from django import forms
from .models import Liga, Equipo, Jugador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = ["nombre"]


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "liga"]


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "equipo"]


class LigaSearchForm(forms.Form):
    query = forms.CharField(label="Buscar liga", max_length=255)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", help_text="Por favor, introduce tu correo electrónico.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de Usuario"
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmación de contraseña"
        self.fields["username"].help_text = (
            "Requerido. 150 caracteres o menos. Solo se permiten letras, dígitos y los siguientes caracteres: @/./+/-/_"
        )
        self.fields["password1"].help_text = "Tu contraseña debe tener al menos 8 caracteres."
        self.fields["password2"].help_text = "Repite la misma contraseña."


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "Por favor, introduce un nombre de usuario y contraseña correctos. "
            "Ten en cuenta que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
        ),
        "inactive": _("Esta cuenta está inactiva."),
    }
