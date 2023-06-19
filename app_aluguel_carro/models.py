from django.db import models

class Cadastro(models.Model):
    id_cadastro = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    idade = models.IntegerField()
    gmail = models.TextField(max_length=200)
    cpf = models.IntegerField()
    cnh = models.IntegerField()
