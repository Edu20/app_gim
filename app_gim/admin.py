from django.contrib import admin

# Register your models here.
from app_gim.models import Alumnos, Clases, Profesores


admin.site.register(Alumnos)
admin.site.register(Clases)
admin.site.register(Profesores)