from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)


def customer(request, **kwargs):

    customer = Customer.objects.get(id = kwargs['id'])

    orders = customer.order_set.all()
    orders_num = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'orders_num': orders_num
    }

    return render(request, 'accounts/customer.html', context)


def products(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'accounts/products.html', context)


def createOrder(request):

    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, **kwargs):

    order = Order.objects.get(id = kwargs['id'])
    form = OrderForm(instance = order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, **kwargs):

    order = Order.objects.get(id = kwargs['id'])

    if request.method == "POST":
        if request.POST.get('Yes'):
            order.delete()

        return redirect('/')


    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)