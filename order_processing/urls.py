from django.urls import path, include
from order_processing import views
urlpatterns = [
    path('', views.home, name='home'),
]
