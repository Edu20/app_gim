from django.shortcuts import render

# Create your views here.






def listar_alumnos(request):
    contexto = {
        "alumnos": [
            {"nombre":"Edu","apellido":"Aguirre"},
            {"nombre":"Marcos","apellido":"Guerra"},
            {"nombre":"Penelope","apellido":"Cruz"}
        ]
    }
    http_response = render(
        request=request,
        template_name="app_gim/listaAlumnos.html",
        context=contexto
    )
    return http_response


def listar_clases(request):
    contexto = {
        "clases": [
            {"nombre":"Aerobox","dia":"Lunes y Miercoles", "horarios":"de 18hs a 19hs"},
            {"nombre":"Spining","dia":"Martes y Jueves", "horarios":"de 18hs a 19hs"},
            {"nombre":"Aerobic","dia":"Lunes y Miercoles", "horarios":"de 19hs a 20hs"}
        ]
    }
    http_response = render(
        request=request,
        template_name="app_gim/listaClases.html",
        context=contexto
    )
    return http_response
