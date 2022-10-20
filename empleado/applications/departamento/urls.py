from django.contrib import admin
from django.urls import path
from . import views
from applications import departamento
from django.apps import AppConfig

class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "applications.departamento"


app_name = 'departamento_app'

urlpatterns = [
    
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
    path('departamento-lista/', views.DepartamentoListView.as_view(), name = 'departamento_list'),
]