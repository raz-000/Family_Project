from django.urls import path 
from Family_App import views

urlpatterns = [
    path('', views.family, name='family'),
    path('index.html', views.inicio_formulario, name='formulario'),
    path('generic.html', views.family_ingress, name='family_ingress'),
    path('formulario/', views.formulario, name='formulario'),
    path('home/', views.padre, name='home'),
    path('home.html', views.padre, name='home'),
]

