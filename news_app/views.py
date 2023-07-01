from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# from .models import *
# from .form import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def home(request):
    
    context ={
        'orders':"orders",
        'customers':"customers",
        'last_five_order':"last_five_order",
        'total_orders':12,
        'total_customers':10,
        'delivered':False,
        'pending':True
    }
    return render(request, 'news/index.html', context)
