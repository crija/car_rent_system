
from django.contrib import admin
from django.urls import path
from app_aluguel_carro import views

urlpatterns = [
    path('dados', views.dados, name = 'dados'),

    path('cadastros/', views.cadastros, name = 'informações_cadastradas'),

    path('preferencias/', views.preferencias, name ='informações_preferenciais'),

   
]
