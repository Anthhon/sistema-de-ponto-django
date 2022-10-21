from django.contrib import admin
from .models import Cargo, Funcionario, Genero, CheckIn

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Cargo)
# admin.site.register(Genero)
admin.site.register(CheckIn)