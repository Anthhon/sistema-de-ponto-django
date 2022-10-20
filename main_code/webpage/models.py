from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CharField, DateField, IntegerField, Model, ForeignKey, TimeField, RESTRICT, CASCADE)
from django.db import models

class Genero(Model):
    Genero = CharField(max_length=35)
    def __str__(self):
        return self.Genero

class Cargo(Model):
    cargo = CharField(max_length=50)
    def __str__(self):
        return self.cargo

# Create your models here.
class Funcionario(Model):
    nome = CharField(max_length=32)
    sobrenome = CharField(max_length=32)
    admissão = DateField()
    cargo = ForeignKey(Cargo, on_delete=RESTRICT,default="Sem_cargo_denifido",blank=True,null=True)
    idade = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ]
     )
    genero = CharField(max_length=30,choices=[('m','Masculino'),('f','Feminino'),('NA','Prefiro não opinar')])
    aniversário = DateField()
    endereço = CharField(max_length=75)
    CPF = IntegerField()

    def __str__(self):
        return (f"{self.nome} {self.sobrenome}")

class CheckIn(Model):
    funcionario = ForeignKey(Funcionario, on_delete=RESTRICT)
    dia = DateField()
    entrada_manhã = TimeField(auto_now=False, auto_now_add=False, default=None, null=True)
    saida_manhã = TimeField(auto_now=False, auto_now_add=False, default=None, null=True)
    entrada_tarde = TimeField(auto_now=False, auto_now_add=False, default=None, null=True)
    saida_tarde = TimeField(auto_now=False, auto_now_add=False, default=None, null=True)

    def __str__(self):
        return (f"{self.funcionario} - {self.dia}")
