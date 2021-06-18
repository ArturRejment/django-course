from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),


    path('', views.dashboard, name='dashboard'),
    path('user/', views.userPage, name='user'),

    path('customer/<int:id>', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('account/', views.accountSettings, name='account'),

    path('create_order/<int:id>', views.createOrder, name='create_order'),
    path('update_order/<int:id>', views.updateOrder, name='update_order'),
    path('delete_order/<int:id>', views.deleteOrder, name='delete_order'),
]


'''
TODO: 1 - Submit email form                         //PasswordResetView.as_view()
TODO: 2 - Email sent success message                //PasswordResetDoneView.as_view()
TODO: 3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
TODO: 4 - Password successfully changed message     // PasswordResetCompleteView.as_view()
'''
