from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime



def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog-single-sidebar.html')





