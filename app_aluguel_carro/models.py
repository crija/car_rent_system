from django.db import models

class Car(models.Model):
    color = models.TextField(max_length=100)
    model = models.TextField(max_length=200)
    brand = models.TextField(max_length=200)
    year = models.IntegerField()
    rented = models.BooleanField(default=False)
    rented_at = models.DateTimeField(null=True)
    rented_until = models.DateTimeField(null=True)
    picture = models.TextField()