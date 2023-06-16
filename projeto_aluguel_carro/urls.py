
from django.contrib import admin
from django.urls import path
from app_aluguel_carro import views

urlpatterns = [
    path('', views.necessidades, name = 'necessidades'),

    path('cadastro/', views.cadastro, name = 'dados_cadastrados')
]
