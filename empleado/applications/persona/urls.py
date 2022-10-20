from django.contrib import admin
from django.urls import path
from . import views
from .models import Persona
from .views import (ListAllEmpleados, SucessView, ListByAreaEmpleado, ListEmpleadoByKword, ListHabilidadesPersona,PersonaDetailView, EmpleadoCreateView)

from django.apps import AppConfig

class Persona(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "application.persona"

def DesdeApps(self):
    print("-------------Desde la app persona-------------")

app_name = 'persona_app'

urlpatterns = [
    path("persona/", DesdeApps),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name="empleados_all"),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view(), name="empleado_area"),
    path('success/', views.SucessView.as_view()),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),    
    path('lista-habilidades-empleado/', views.ListHabilidadesPersona.as_view()),
    path('ver-empleado/<pk>', views.PersonaDetailView.as_view(), name="empleado_detail"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="empleado_add"),
    path('success/', views.SucessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name= 'modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name= 'eliminar_empleado'),
    path('', views.InicioView.as_view(), name= 'inicio'),
    path('lista-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name= 'empleados_admin'),
]   

