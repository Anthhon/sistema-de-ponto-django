from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, DateField, IntegerField, Model, ForeignKey, RESTRICT, CASCADE
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
        return (f"{self.nome} {self.sobrenome} - {self.cargo}")


class Horario(Model):
    horario_inicio_manha = models.DateTimeField(auto_now_add=False)
    horario_fim_manha = models.DateTimeField(auto_now=False, auto_now_add=False)
    horario_inicio_tarde = models.DateTimeField(auto_now=False, auto_now_add=False)
    horario_fim_tarde = models.DateTimeField(auto_now=False, auto_now_add=False)
    funcionario = ForeignKey(Funcionario, on_delete=CASCADE)
    def __str__(self):
        return (f"{self.funcionario.nome} {self.horario}")