from django.shortcuts import render, redirect
from datetime import datetime
from order_processing.models import Food, Employee, Order, FoodOrder


def home(request):
    food = Food.objects.all()
    employee = Employee.objects.all()
    if request.method == 'POST':
        selected_food_ids = request.POST.getlist('food')
        employee_id = request.POST.get('employee')
        date = request.POST.get('datetime')

        selected_foods = Food.objects.filter(id__in=selected_food_ids)
        employee_name = Employee.objects.get(id=employee_id)
        total_price = sum(food.cost for food in selected_foods)

        order = Order()
        order.employee = employee_name
        order.date = datetime.fromisoformat(date)
        order.save()

        food_order = FoodOrder()
        food_order.order = order
        food_order.total_cost = total_price
        food_order.save()
        food_order.food.set(selected_foods)

        return redirect(home)
    return render(request, 'index.html', {'foods': food, 'employees': employee})
