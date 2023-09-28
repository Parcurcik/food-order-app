from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Сотрудник')

    def __str__(self):
        return self.name


class Food(models.Model):
    food_name = models.CharField(max_length=40, verbose_name='Названия блюда')
    composition = models.CharField(max_length=100, verbose_name='Состав')
    cost = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'Название: {self.food_name}, Состав: {self.composition}, Цена: {self.cost}'


class Order(models.Model):
    date = models.DateTimeField(verbose_name="Дата и время")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Заказчик')

    def __str__(self):
        return f'Дата: {self.date.strftime("%Y-%m-%d")}; Время: {self.date.strftime("%H:%M")}; Заказчик: {self.employee}'


class FoodOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    food = models.ManyToManyField(Food, verbose_name='Блюда')
    total_cost = models.IntegerField(verbose_name='Сумма заказа')

    def __str__(self):
        return f'{self.order}; Блюда: {", ".join([food.food_name for food in self.food.all()])}; Стоимость заказа: {self.total_cost} руб.'
