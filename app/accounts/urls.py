from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer/<int:id>', views.customer, name='customer'),
    path('products/', views.products, name='products')
]
