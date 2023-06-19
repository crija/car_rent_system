from django.shortcuts import render
from .models import Cadastro


def necessidades(request):
    return render(request, 'cadastro/necessidades.html')

def cadastro(request):
    #Salvar os dados da tela para o banco de dados.
    novo_cadastro = Cadastro()
    novo_cadastro.nome = request.POST.get('nome')
    novo_cadastro.idade = request.POST.get('idade')
    novo_cadastro.cpf = request.POST.get('cpf')
    novo_cadastro.cnh = request.POST.get('cnh')
    novo_cadastro.gmail = request.POST.get('gmail')
    novo_cadastro.save()

    #Exibir todos os usuários já cadastrados em uma nova página.
    cadastro = {
        'cadastro':Cadastro.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request, 'cadastro/cadastro.html', cadastro)