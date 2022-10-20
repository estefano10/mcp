from msilib.schema import ListView
from django.shortcuts import render
from django.apps import AppConfig

#from empleado.applications.home.forms import PruebaForm
from .models import Prueba
from applications.home.forms import PruebaForm

# invoco a la clase de vistas de plantillas.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView



#creo una clase prueba view basada en la clase generica templateview
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "home"

class PruebaView(TemplateView):
#     #le pasamos el nombre de la plantilla
    template_name = "home/prueba.html"

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset= ['0', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    context_object_name = 'lista'
    model = Prueba

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '/'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'
   

    

# class ModelListview(ListView):
#     model = Model 
#     template_name = ".html"