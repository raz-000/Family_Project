from django.shortcuts import render
from django.http import HttpResponse # Necesario para Generar respuestas sobre http
from .models import *
from .forms import *
# Create your views here.

# def family(request):
#     return HttpResponse("HOLA!!! Esta es la familia!.")

def family(request):
    return render(request, "index3.html")

def family_ingress(request):
    return render(request, "index.html")

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

        # miFormulario = Formularios_Family(request.POST)
        # print(miFormulario)

        # if miFormulario.is_valid:
        #     informacion = miFormulario.cleaned_data
        #     familia = Integrante_Familia(nombre=informacion['nombre'], profesion=informacion['profesion'], edad=informacion['edad'], email=informacion['email'], descripcion=informacion['descripcion'])
        #     familia.save()
        #     return render(request, "index3_formulario.html")


# #       return HttpResponse(request.POST.items())
#         formulario = Integrante_Familia(request.POST['nombre'], request.POST['profesion'], request.POST['edad'], request.POST['email'], request.POST['descripcion'])
#         # return f'Esta funcionando {nombre}'
#         formulario.save()
#         return render(request, "index3_formulario.html")
#