from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from .filters import *
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

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'orders_num': orders_num,
        'order_filter': myFilter
    }

    return render(request, 'accounts/customer.html', context)


def products(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'accounts/products.html', context)


def createOrder(request, **kwargs):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)

    customer = Customer.objects.get(id = kwargs['id'])

    formSet = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial = {'customer':customer})

    if request.method == "POST":
        formSet = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formSet.is_valid():
            formSet.save()
            return redirect('/')


    context = {'formset': formSet}
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


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)