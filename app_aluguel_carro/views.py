from django.shortcuts import render
from .models import Cadastros


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

    #Exibir todos os usuários já cadastrados em uma nova página.
    cadastros = {
        'cadastros':Cadastros.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'cadastros/cadastros.html', cadastros)