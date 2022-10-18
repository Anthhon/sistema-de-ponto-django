from django.db import models


# Create your models here.

class Endereco(models.Model):
    rua = models.CharField()
    bairro = models.CharField()
    numero = models.IntegerField()
    complemento = models.CharField()


class Funcionario(models.Model):
    primeiro_nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    cpf = models.IntegerField(max_length=11)
    idade = models.IntegerField(max_length=3)
    nascimento = models.DateTimeField(auto_now_add=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING, related_name="funcionario")


"""
Primeiro nome
    Sobrenome
    Data de admissão
    Idade
    Sexo
    Data de aniversário
    Endereço
    CPF
"""
