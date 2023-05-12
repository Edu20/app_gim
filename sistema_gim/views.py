from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}/{hoy.year}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_usuario(request, nombre):
    saludo = f"Hola {nombre}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto = {
        "usuario":"Eduardo"
    }
    http_response = render(
        request=request,
        template_name="app_gim/base.html",
        context=contexto
    )
    return http_response