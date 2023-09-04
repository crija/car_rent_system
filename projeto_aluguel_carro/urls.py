from django.contrib import admin
from django.urls import path
from app_aluguel_carro import views

urlpatterns = [
   path('cars', views.cars, name='cars'),
   path('admin/cars', views.create_car, name='create_car')
   
]
