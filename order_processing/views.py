from django.shortcuts import render
from order_processing.models import Food, Employee


def home(requests):
    food = Food.objects.all()
    employee = Employee.objects.all()
    return render(requests, 'index.html', {'foods': food, 'employees': employee} )
