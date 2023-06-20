from django.db import models

class Cadastros(models.Model):
    id_cadastro = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    idade = models.IntegerField()
    gmail = models.TextField(max_length=200)
    cpf = models.IntegerField()
    cnh = models.IntegerField()

class Preferencias(models.Model):
    id_preferencias = models.AutoField(primary_key=True)
    cidade_retirada = models.TextField(max_length=100)
    dia_retirada = models.IntegerField()
    dia_devolução = models.IntegerField()
    tamanho = models.TextField(max_length=1)
    cor = models.TextField(max_length=50)