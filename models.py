from django.db import models

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
        ('cashier', 'Cashier'),
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='waiter')
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.date} {self.time}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    table_number = models.PositiveIntegerField(blank=True, null=True)

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    def get_subtotal(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=30)  # e.g., kg, litre, piece
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipes')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return f"{self.product.name} needs {self.quantity_needed} {self.ingredient.unit} of {self.ingredient.name}"


class Stock(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    quantity_available = models.DecimalField(max_digits=10, decimal_places=3)
    minimum_threshold = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def is_low(self):
        return self.quantity_available <= self.minimum_threshold

    def __str__(self):
        return f"{self.ingredient.name}: {self.quantity_available} {self.ingredient.unit}"
