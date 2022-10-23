from django.contrib import admin
from .models import Cargo, Funcionario, CheckIn

admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(CheckIn)