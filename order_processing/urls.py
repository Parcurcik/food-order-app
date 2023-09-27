from django.urls import path
from order_processing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download', views.make_report, name='report')
]
