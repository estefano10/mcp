from django.contrib import admin
from django.urls import path
from django.apps import AppConfig
from . import views


urlpatterns = [
    path("prueba/", views.PruebaView.as_view(), name='prueba'),
    path('lista/', views.PruebaListView.as_view(), name='pruebalista'),
    path('listar_prueba', views.ListarPrueba.as_view(), name='listarprueba'),
    path("add/", views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name='resume_foundation'),

]