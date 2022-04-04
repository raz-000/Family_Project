from django.shortcuts import render
from django.http import HttpResponse # Necesario para Generar respuestas sobre http
from .models import *
# Create your views here.

# def family(request):
#     return HttpResponse("HOLA!!! Esta es la familia!.")

def family(request):
    return render(request, "home.html")

def inicio_formulario(request):
    return render(request, "index3.html")


def family_ingress(request):

    person = Integrante_Familia.objects.all()
    familiar = {

    }
    print('--------------------------------------------------------------------')
    print(person)
    
    return render(request, "index.html", {"person":person})

def formulario(request):
#    if request.method == 'POST':
    print('----------------------------------------')
    print(request.POST)

    nombre = request.POST['nombre']
    profesion = request.POST['profesion']
    edad = request.POST['edad']
    email = request.POST['email']
    descripcion = request.POST['descripcion']

    nuevo_inegrante = Integrante_Familia(nombre=nombre, profesion=profesion, edad=edad, email=email, descripcion=descripcion)
    nuevo_inegrante.save()

    return render(request, "index3_formulario.html", {'nombre': nombre})

def padre(request):
    return render(request, "home.html")