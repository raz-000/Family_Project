from django.shortcuts import render
from django.http import HttpResponse # Necesario para Generar respuestas sobre http
# Create your views here.

# def family(request):
#     return HttpResponse("HOLA!!! Esta es la familia!.")

def family(request):
    return render(request, "index3.html")

def family_ingress(request):
    return render(request, "index.html")
