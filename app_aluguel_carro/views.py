from django.shortcuts import render
from .models import Cadastros
from .models import Preferencias


def dados(request):
    return render(request, 'cadastros/dados.html')

def cadastros(request):
    #Salvar os dados da tela para o banco de dados.
    novo_cadastros = Cadastros()
    novo_cadastros.nome = request.POST.get('nome')
    novo_cadastros.idade = request.POST.get('idade')
    novo_cadastros.cpf = request.POST.get('cpf')
    novo_cadastros.cnh = request.POST.get('cnh')
    novo_cadastros.gmail = request.POST.get('gmail')
    novo_cadastros.save()

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'cadastros/preferencias.html')

def preferencias(request):
    nova_preferencia = Preferencias()
    nova_preferencia.cidade_retirada = request.POST.get('cidade')
    nova_preferencia.dia_retirada = request.POST.get('dia_retirada')
    nova_preferencia.dia_devolução = request.POST.get('dia_devolução')
    nova_preferencia.tamanho = request.POST.get('tamanho')
    nova_preferencia.cor = request.POST.get('cor')
    nova_preferencia.save()

    
    dados = {
        'preferencias':Preferencias.objects.all(),
        'cadastros':Cadastros.objects.all()
    }

    return render(request, 'cadastros/cadastros.html', dados)
