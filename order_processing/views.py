from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from datetime import datetime
import random

from order_processing.models import Food, Employee, Order, FoodOrder


def home(request):
    food = Food.objects.all()
    employee = Employee.objects.all()
    if request.method == 'POST':
        selected_food_ids = request.POST.getlist('food')
        employee_id = request.POST.get('employee')
        date = request.POST.get('datetime')
        if selected_food_ids == ['0']:
            num_selected = random.randint(1, Food.objects.count())
            selected_foods = random.sample(list(food), num_selected)
        else:
            selected_foods = Food.objects.filter(id__in=selected_food_ids)

        if not selected_foods:
            messages.error(request, 'Для заказа нужно выбрать как минимум одно блюдо!')
            return redirect('home')
        employee_name = Employee.objects.get(id=employee_id)
        total_price = sum(food.cost for food in selected_foods)

        order = Order()
        order.employee = employee_name
        order.date = timezone.make_aware(datetime.fromisoformat(date), timezone=timezone.get_current_timezone())
        order.save()

        food_order = FoodOrder()
        food_order.order = order
        food_order.total_cost = total_price
        food_order.save()
        food_order.food.set(selected_foods)

        messages.success(request, 'Ваш заказ успешно оформлен!')
        return redirect(home)
    return render(request, 'index.html', {'foods': food, 'employees': employee})


def make_report(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date_to_report')
        food_orders = FoodOrder.objects.filter(order__date__date=selected_date)
        total_cost_of_all_orders = sum(order.total_cost for order in food_orders)
        context = {
            'date': selected_date,
            'food_orders': food_orders,
            'total_cost': total_cost_of_all_orders,
        }
        return render(request, 'report.html', context)



