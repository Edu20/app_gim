from django.contrib import admin
from django.urls import path
from app_gim.views import listar_alumnos, listar_clases



urlpatterns = [
    path('alumnos/', listar_alumnos),
    path('clases/', listar_clases),
]