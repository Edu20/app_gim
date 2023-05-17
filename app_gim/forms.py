from django import forms

class ClaseFormulario(forms.Form):
    nombre = forms.CharField(max_length=164, required=True)
    dia = forms.CharField(max_length=50, required=True)
    horario = forms.CharField(max_length=50, required=True)