from django.shortcuts import render

# Create your views here.

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