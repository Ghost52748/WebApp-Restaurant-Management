from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Employee, Product, Order, OrderItem, Reservation, Supplier, Ingredient, Stock
from django.contrib import messages

# ─── PRODUCT VIEWS ─────────────────────────────────────────────────────────────

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST.get('description', ''),
            price=request.POST['price'],
        )
        messages.success(request, 'Product added successfully.')
        return redirect('product_list')
    return render(request, 'core/product_form.html')

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST.get('description', '')
        product.price = request.POST['price']
        product.save()
        messages.success(request, 'Product updated.')
        return redirect('product_list')
    return render(request, 'core/product_form.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect('product_list')

# ─── CUSTOMER VIEWS ─────────────────────────────────────────────────────────────

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'core/customer_list.html', {'customers': customers})

def customer_add(request):
    if request.method == 'POST':
        Customer.objects.create(
            name=request.POST['name'],
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
        )
        messages.success(request, 'Customer added.')
        return redirect('customer_list')
    return render(request, 'core/customer_form.html')

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customer_list')
    return render(request, 'core/customer_form.html', {'customer': customer})

def customer_delete(request, pk):
    get_object_or_404(Customer, pk=pk).delete()
    return redirect('customer_list')

# ─── EMPLOYEE VIEWS ─────────────────────────────────────────────────────────────

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            role=request.POST['role'],
            hire_date=request.POST['hire_date'],
            salary=request.POST['salary'],
        )
        messages.success(request, 'Employee added.')
        return redirect('employee_list')
    return render(request, 'core/employee_form.html')

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.role = request.POST['role']
        employee.hire_date = request.POST['hire_date']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')
    return render(request, 'core/employee_form.html', {'employee': employee})

def employee_delete(request, pk):
    get_object_or_404(Employee, pk=pk).delete()
    return redirect('employee_list')

# ─── ORDER VIEWS ────────────────────────────────────────────────────────────────

def order_list(request):
    orders = Order.objects.all().prefetch_related('items__product')
    return render(request, 'core/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        table_number = request.POST.get('table_number')
        order = Order.objects.create(
            customer_id=customer_id if customer_id else None,
            table_number=table_number,
        )
        product_ids = request.POST.getlist('product_id')
        quantities = request.POST.getlist('quantity')
        for pid, qty in zip(product_ids, quantities):
            product = get_object_or_404(Product, pk=pid)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=int(qty),
                unit_price=product.price,
            )
        messages.success(request, f'Order #{order.id} created.')
        return redirect('order_list')
    customers = Customer.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'core/order_form.html', {'customers': customers, 'products': products})

def order_delete(request, pk):
    get_object_or_404(Order, pk=pk).delete()
    return redirect('order_list')

# ─── RESERVATION VIEWS ──────────────────────────────────────────────────────────

def reservation_list(request):
    reservations = Reservation.objects.select_related('customer').all()
    return render(request, 'core/reservation_list.html', {'reservations': reservations})

def reservation_add(request):
    if request.method == 'POST':
        Reservation.objects.create(
            customer_id=request.POST['customer'],
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests'],
        )
        return redirect('reservation_list')
    customers = Customer.objects.all()
    return render(request, 'core/reservation_form.html', {'customers': customers})

def reservation_delete(request, pk):
    get_object_or_404(Reservation, pk=pk).delete()
    return redirect('reservation_list')

# ─── STOCK VIEWS ─────────────────────────────────────────────────────────────────

def stock_list(request):
    stocks = Stock.objects.select_related('ingredient').all()
    return render(request, 'core/stock_list.html', {'stocks': stocks})