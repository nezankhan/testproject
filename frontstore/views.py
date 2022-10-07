from django.shortcuts import render
from .models import Inventory
# Create your views here.

def home(request):
    context = {
        'inventory': Inventory.objects.all()
    }
    return render(request,'frontstore/home.html',context)