from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def customer(request):
    return render(request, 'accounts/customer.html')


def products(request):
    return render(request, 'accounts/products.html')
