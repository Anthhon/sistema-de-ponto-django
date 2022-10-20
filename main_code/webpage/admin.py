from django.contrib import admin
from .models import Cargo, Funcionario, Gênero, CheckIn

from .models import Cargo, Funcionario, Genero

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Gênero)
admin.site.register(CheckIn)