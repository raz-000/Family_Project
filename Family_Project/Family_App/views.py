from django.shortcuts import render
from django.http import HttpResponse # Necesario para Generar respuestas sobre http
from .models import *
from Family_App.forms import *
# Create your views here.

# def family(request):
#     return HttpResponse("HOLA!!! Esta es la familia!.")

def family(request):
    return render(request, "home.html")

def inicio_formulario(request):
    return render(request, "index3.html")


def family_ingress(request):

    person = Integrante_Familia.objects.all()
    mascota1 = Mascota.objects.all()
    alimento1 = Alimento.objects.all()
    print('--------------------------------------------------------------------')
    print(mascota1[0])
    print(person[0])
    return render(request, "index.html", {"person":person, 'mascota1':mascota1, 'alimento1':alimento1})

def formulario(request):
    # print(request.POST)
    # nombre = request.POST['nombre']
    # nombre_mascota=request.POST['nombre_mascota']
    # edad_mascota=request.POST['edad_mascota']
    # if request.method == 'POST':
    #     miFormulario = FormularioPersona(request.POST)
    #     print(miFormulario)
    #     if miFormulario.is_valid:
    #         informacion = miFormulario.cleaned_data

    #         nuevo_inegrante = Integrante_Familia(nombre=informacion['nombre'], profesion=['profesion'], edad=['edad'], email=['email'], descripcion=['descripcion'], nombre_mascota=['nombre_mascota'])
    #         nuevo_inegrante.save()

    #         nueva_mascota = Mascota(nombre_mascota=['nombre_mascota'], edad_mascota=['edad_mascota'], raza_mascota=['raza_mascota'])
    #         nueva_mascota.save()

    #         nuevo_alimento = Alimento(marca_alimento=['marca_alimento'], precio_dolares=['precio_dolares'])
    #         nuevo_alimento.save()

    #         return render(request, "index3_formulario.html", {'nombre': nombre, 'nombre_mascota':nombre_mascota, 'edad_mascota':edad_mascota})

    print('----------------------------------------++++++++++++++++++++++++++++++++++++++++')
    

    nombre = request.POST['nombre']
    profesion = request.POST['profesion']
    edad = request.POST['edad']
    email = request.POST['email']
    descripcion = request.POST['descripcion']
    nombre_mascota=request.POST['nombre_mascota']
    edad_mascota=request.POST['edad_mascota']
    raza_mascota=request.POST['raza_mascota']
    marca_alimento=request.POST['marca_alimento']
    precio_dolares=request.POST['precio_dolares']


    nuevo_inegrante = Integrante_Familia(nombre=nombre, profesion=profesion, edad=edad, email=email, descripcion=descripcion, nombre_mascota=nombre_mascota)
    nuevo_inegrante.save()

    nueva_mascota = Mascota(nombre_mascota=nombre_mascota, edad_mascota=edad_mascota, raza_mascota=raza_mascota)
    nueva_mascota.save()

    nuevo_alimento = Alimento(marca_alimento=marca_alimento, precio_dolares=precio_dolares)
    nuevo_alimento.save()

    return render(request, "index3_formulario.html", {'nombre': nombre, 'nombre_mascota':nombre_mascota, 'edad_mascota':edad_mascota})

def padre(request):
    return render(request, "home.html")

def generic(request):
    return render(request, "generic1.html")