# WebApp-Restaurant-Management
django-mysql-project
# Restaurant Management Web Application

## Project Overview

This project is a web-based Restaurant Management System developed using Django (Python) and MySQL. It is designed to help restaurants manage daily operations such as products, customers, orders, employees, and inventory through a centralized system.

The application replaces manual processes with a structured digital solution to improve efficiency, accuracy, and decision-making.


## Project Objectives

### Main Objective

Develop a functional web application that simplifies restaurant management tasks.

### Specific Objectives

* Design and integrate a relational database (MySQL)
* Develop backend logic using Django
* Create user-friendly interfaces
* Manage operations: products, customers, orders, employees, and inventory
* Ensure system security and efficiency


## Current Features (Implemented)

### Product Management Module

* Add product
* View product list
* Update product
* Delete product

### In Progress

* Customer management
* Order processing
* Reservation system
* Inventory management
* Dashboard


## Technologies Used

* Backend: Django (Python)
* Database: MySQL
* Frontend: HTML, CSS
* Tools: GitHub, VS Code


## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Ghost52748/WebApp-Restaurant-Management.git
```

2. Navigate into the project:

```bash
cd WebApp-Restaurant-Management
```

3. Create a virtual environment:

```bash
conda create -n django_env python=3.11
conda activate django_env
```

4. Install dependencies:

```bash
pip install django mysqlclient
```

5. Configure the MySQL database in `settings.py`.

6. Apply migrations:

```bash
python manage.py migrate
```

7. Run the server:

```bash
python manage.py runserver
```

8. Open in a browser:

```
http://127.0.0.1:8000/
```


## Project Modules

* Product Management
* Customer Management (in progress)
* Order Management (in progress)
* Reservation Management (planned)
* Employee Management (planned)
* Inventory Management (planned)


## System Features (Target)

* Role-based access (Admin, Staff, etc.)
* Order tracking and billing
* Inventory alerts
* Financial dashboard
* Secure authentication


## Team Members

* Kamdem Matchum Judith: Documentation, Database Analysis, README file creation, Coordination
* Mvondo Mvondo Wilfried Anthony: Backend Development
* Massado Djoko Aicha: Frontend Development
* Mep Meku Audrey: Integration and Testing
* Ibrahim Diallo: System Analysis and Implementation Support


## Project Status

Currently in development ( System Development)


## License

This project is for academic purposes.
