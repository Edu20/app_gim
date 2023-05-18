from django.shortcuts import render, redirect
from django.urls import reverse

from app_gim.forms import ClaseFormulario
from app_gim.models import Clases, Profesores, Alumnos
# Create your views here.






def listar_alumnos(request):
    contexto = {
        "alumnos": Alumnos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="app_gim/listaAlumnos.html",
        context=contexto
    )
    return http_response


def listar_clases(request):
    contexto = {
        "clases": Clases.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="app_gim/listaClases.html",
        context=contexto
    )
    return http_response


def crear_clase1(request):
    if request.method == "POST":
        data = request.POST # es un diccionario
        nombre = data["nombre"]
        dia = data["dia"]
        horario = data["horario"]
        clase = Clases(nombre=nombre,dia=dia,horario=horario) #se crea en RAM
        clase.save() #se guarda en la base de datos 
        url_exitosa = reverse('lista_clases')
        return redirect(url_exitosa)
    
    else:
        http_response = render(
        request=request,
        template_name="app_gim/formulario_a_mano.html",
        )
        return http_response

    

def crear_clase(request):
    if request.method == "POST":
        formulario = ClaseFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data # es un diccionario
            nombre = data["nombre"]
            dia = data["dia"]
            horario = data["horario"]
            clase = Clases(nombre=nombre,dia=dia,horario=horario) #se crea en RAM
            clase.save() #se guarda en la base de datos 
            url_exitosa = reverse('lista_clases')
            return redirect(url_exitosa)
        
    
    else:
        formulario =ClaseFormulario()
        http_response = render(
        request=request,
        template_name="app_gim/formulario_clase.html",
        context={'formulario':formulario}
        )
        return http_response
    

def buscar_clases(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        clases = Clases.objects.filter(nombre=busqueda)
        contexto = {
            "clases": clases,
        }
    http_response = render(
        request=request,
        template_name='app_gim/listaClases.html',
        context=contexto,
    )
    return http_response
        

