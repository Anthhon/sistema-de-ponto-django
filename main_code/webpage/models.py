from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, DateField, IntegerField, Model


# Create your models here.
class Funcionario(Model):
    nome = CharField(max_length=12)
    sobrenome = CharField(max_length=15)
    admissão = DateField()
    cargo = CharField(max_length=25)
    idade = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ]
     )
    gênero = CharField(max_length=20)
    aniversário = DateField()
    endereço = CharField(max_length=75)
    CPF = IntegerField()#max_length' is ignored when used with IntegerField.

# Coloca o nome e cargo do funcionário como o próprio título na tela de administrador
    def __str__(self):
        return (f"{self.nome} {self.sobrenome} - {self.cargo}")
