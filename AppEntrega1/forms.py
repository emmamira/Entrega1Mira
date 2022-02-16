from socket import fromshare
from django import forms

class LigaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    cantidadEquipos=forms.IntegerField()