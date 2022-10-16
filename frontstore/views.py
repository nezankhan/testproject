from django.shortcuts import render
from .models import Inventory, PurchaseOrders, SaleOrders
# Create your views here.

def home(request):
    context = {
        'inventory': Inventory.objects.all(),
        
    }
    return render(request,'frontstore/home.html',context)

def staff(request):
    return render(request,'frontstore/staff.html',{'title':'title'})


def orders(request):
    
    context = {
        'saleorders':SaleOrders.objects.all(),
    }
    return render(request,'frontstore/orders.html',context)