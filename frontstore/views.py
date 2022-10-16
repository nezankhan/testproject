from django.shortcuts import render
from .models import Inventory, PurchaseOrders
# Create your views here.

def home(request):
    context = {
        'inventory': Inventory.objects.all()
    }
    return render(request,'frontstore/home.html',context)

def staff(request):
    return render(request,'frontstore/staff.html',{'title':'title'})


def orders(request):
    
    context = {
        'inventory': PurchaseOrders.objects.all()
    }
    return render(request,'frontstore/orders.html',context)