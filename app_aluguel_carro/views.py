from django.shortcuts import render
from .models import Car

def cars(request):
    if request.method == "POST":
        new_car = Car()
        new_car.color = request.POST.get('color')
        new_car.model = request.POST.get('model')
        new_car.brand = request.POST.get('brand')
        new_car.year = request.POST.get('year')
        new_car.picture = request.POST.get('picture')
        new_car.save()

    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)

def create_car(request):
   return render(request, 'cars/create_car.html')