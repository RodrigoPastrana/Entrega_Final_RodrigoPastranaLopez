from django import forms
from .models import Liga, Equipo, Jugador


class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = ["nombre"]


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "division"]


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "equipo"]


class LigaSearchForm(forms.Form):
    query = forms.CharField(label="Buscar liga", max_length=255)
