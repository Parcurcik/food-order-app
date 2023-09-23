from django.contrib import admin
from order_processing.models import Employee, Order, Food, FoodOrder

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(FoodOrder)
