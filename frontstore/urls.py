from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name='home'),
    path('staff/',views.staff,name='staff'),
    path('orders/',views.orders,name='orders'),
]