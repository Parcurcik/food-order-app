from django.contrib import admin
from .models import Employee, Food, Order, FoodOrder


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'composition', 'cost')
    list_filter = ('food_name', 'cost')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'employee')
    list_filter = ('date', 'employee')


class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('get_order_date', 'get_order_time', 'get_order_customer', 'get_food_names', 'total_cost')
    list_filter = ('order__date', 'order__employee', 'total_cost')

    def get_order_date(self, obj):
        return obj.order.date.strftime("%Y-%m-%d")

    def get_order_time(self, obj):
        return obj.order.date.strftime("%H:%M")

    def get_order_customer(self, obj):
        return obj.order.employee.name

    def get_food_names(self, obj):
        return ", ".join([food.food_name for food in obj.food.all()])

    get_order_date.short_description = 'Дата'
    get_food_names.short_description = 'Блюда'
    get_order_time.short_description = 'Время'
    get_order_customer.short_description = 'Заказчик'


admin.site.register(Order, OrderAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(FoodOrder, FoodOrderAdmin)
