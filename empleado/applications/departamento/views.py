from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from applications import departamento
from .forms import NewDepartamentoForm
from .models import Departamento
from applications.persona.models import Persona

# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def valid(self, form):
        print("*********** ESTAMOS EN EL FORM VALID********")

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data ['shortname'],

        )
        depa.save()
        
        nombre = form.cleaned_data['nombre'],
        apellidos = form.cleaned_data['apellidos'],
        Persona.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'