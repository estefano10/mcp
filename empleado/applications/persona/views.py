from urllib import request
from unicodedata import name
from django.shortcuts import render
from .forms import EmpleadoForm
from django.core.paginator import Paginator

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Habilidades, Persona

class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')



class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Persona

class ListAllEmpleados(ListView):
    # listar todos los empleados de la empresa
    template_name = "persona/list_all.html"
    paginate_by = 2
    ordering = 'first_name',
    context_object_name = 'empleados'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Persona.objects.filter(
            first_name__icontains= palabra_clave
        )
        return lista

class SucessView(TemplateView):
    template_name = "persona/success.html"

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = "empleados"

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Persona.objects.filter(departamento__short_name = area)
        return lista 

class ListEmpleadoByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('*******************************************')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Persona.objects.filter(first_name = palabra_clave)
        
        return lista

class ListHabilidadesPersona(ListView):
    #model = Persona
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    

    def get_queryset(self):
        persona = Persona.objects.get(id=1)
        return persona.habilidades.all()
        
class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'persona/detail_persona.html'
    # context_object_name = 'lista'
    
    
    def get_context_data(self, **kwargs):
        context = super(PersonaDetailView, self).get_context_data(**kwargs)
        context ['titulo']='Empleado del mes'
        return context


class EmpleadoCreateView(CreateView):
    model = Persona
    template_name = "persona/add.html"
    #fields = ['first_name', 'last_name', 'job']
    #fields = ('__all__')
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' '+ empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form) 

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Persona
    fields = ('first_name' , 'last_name', 'job', 'departamento', 'habilidades', 'avatar')
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')

class InicioView(TemplateView):
    template_name = "inicio.html"
