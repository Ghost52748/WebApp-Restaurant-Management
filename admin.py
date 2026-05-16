from django.contrib import admin
from .models import (
    Customer, Employee, Product, Order, OrderItem,
    Reservation, Supplier, Ingredient, Recipe, Stock
)

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reservation)
admin.site.register(Supplier)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Stock)