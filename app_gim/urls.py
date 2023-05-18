from django.contrib import admin
from django.urls import path
from app_gim.views import listar_alumnos, listar_clases, crear_clase, buscar_clases



urlpatterns = [
    path('alumnos/', listar_alumnos, name="lista_alumnos"),
    path('clases/', listar_clases, name="lista_clases"),
    path('crearClases/', crear_clase, name="crear_clases"),
    path('buscarClases/', buscar_clases, name="buscar_clases"),
]