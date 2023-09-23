from django.contrib import admin
from django.urls import path, include
from order_processing.views import home
urlpatterns = [
    path('', home)
]
