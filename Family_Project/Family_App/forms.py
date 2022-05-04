from django import forms

class FormularioPersona(forms.Form):
    nombre = forms.CharField()
    profesion = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    descripcion = forms.CharField()
    nombre_mascota = forms.CharField()
    edad_mascota = forms.IntegerField()
    raza_mascota = forms.CharField()
    marca_alimento = forms.CharField()
    precio_dolares = forms.CharField()