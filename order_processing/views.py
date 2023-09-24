from django.shortcuts import render
from order_processing.models import Food


def home(requests):
    food = Food.objects.all()
    return render(requests, 'index.html', {'foods': food})
