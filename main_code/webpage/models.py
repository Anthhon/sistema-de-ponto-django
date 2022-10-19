from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, DateField, IntegerField, Model, ForeignKey, RESTRICT, CASCADE

class Gênero(Model):
    gênero = CharField(max_length=35)
    def __str__(self):
        return self.gênero

class Cargo(Model):
    cargo = CharField(max_length=50)
    def __str__(self):
        return self.cargo

# Create your models here.
class Funcionario(Model):
    nome = CharField(max_length=12)
    sobrenome = CharField(max_length=15)
    admissão = DateField()
    cargo = ForeignKey(Cargo, on_delete=RESTRICT)
    idade = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ]
     )
    gênero = ForeignKey(Gênero, on_delete=RESTRICT)
    aniversário = DateField()
    endereço = CharField(max_length=75)
    CPF = IntegerField()

    def __str__(self):
        return (f"{self.nome} {self.sobrenome} - {self.cargo}")
