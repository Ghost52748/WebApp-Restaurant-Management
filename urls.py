from django.urls import path
from . import views

urlpatterns = [
    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Customers
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/edit/<int:pk>/', views.customer_edit, name='customer_edit'),
    path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),

    # Employees
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    # Orders
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),

    # Reservations
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.reservation_add, name='reservation_add'),
    path('reservations/delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),

    # Stock
    path('stock/', views.stock_list, name='stock_list'),
]