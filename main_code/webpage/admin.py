from django.contrib import admin
from .models import Cargo, Funcionario, CheckIn

# Registra os modelos a serem exibidos na página de admin
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(CheckIn)
