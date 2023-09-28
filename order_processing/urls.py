from django.urls import path
from order_processing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report', views.make_report, name='report')
]
