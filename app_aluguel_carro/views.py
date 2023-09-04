from django.shortcuts import render
from .models import Car

def cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)

def create_car(request):
   return render(request, 'cars/create_car.html')