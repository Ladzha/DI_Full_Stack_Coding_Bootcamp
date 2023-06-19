from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation, Address
from .forms import AddCustomerForm, AddRentalForm, AddVihicleForm
import datetime
# Create your views here.


# url /rent/rental/ - show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)
def all_rentals(request):
    all_rentals = Rental.objects.all().order_by('rental_date')
    context = {'all_rentals': all_rentals}
    return render(request, 'all_rentals.html', context)

# url /rent/vehicle/ - show all vehicles, grouped into their groups (‘bike’ and ‘scooter’)
def all_vehicles(request): 
    all_vehicles = Vehicle.objects.all().order_by('vehicle_type')
    context = {'all_vehicles': all_vehicles}
    return render(request, 'all_vehicles.html', context)

# url /rent/customer/ - show all customers, in alphabetical order
def all_customers(request): 
    all_customers = Customer.objects.all().order_by('first_name', 'last_name')
    context = {'all_customers': all_customers}
    return render(request, 'all_customers.html', context)

# url /rent/customer/add – provide a form to add a new customer

def add_customer(request): 
    if request.method == 'POST':
        data = request.POST
        form = AddCustomerForm(data)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    add_customer_form = AddCustomerForm()
    context = {'form': add_customer_form}
    return render(request, 'add_customer.html', context)
# url /rent/rental/add – provide a form to enter a customer ID and a vehicle ID to create a rental. If the customer or the vehicle does not exist, show a user-friendly error message. If the vehicle is currently being rented, show a relevant error message.
def add_rental(request): 
    #POST
    if request.method == 'POST':
        data = request.POST
        form = AddRentalForm(data)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    add_rental_form = AddRentalForm()
    context = {'form': add_rental_form}
    return render(request, 'add_rental.html', context)

# url /rent/vehicle/add – provide a form to add a new vehicle.
def add_vehicle(request): 
    #POST
    if request.method == 'POST':
        data = request.POST
        form = AddVihicleForm(data)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        add_vehicle_form = AddVihicleForm()
    context = {'form': add_vehicle_form}

    return render(request, 'add_vehicle.html', context)

# url /rent/customer/<pk> - show the customer matching the given ID
def customer_info(request, id): 
    customer_info = Customer.objects.get(id=id)
    context = {'customer_info': customer_info}
    return render(request, 'customer_info.html', context)

# url /rent/rental/<pk> - show the information about the given rental:customer details vehicle detailsrental details (“Returned on: <date>” / “Not yet returned”)
def rental_info(request, id): 
    rental_info = Rental.objects.get(id=id)
    if request.method == 'POST':
        rental_info.return_date=datetime.datetime.now()
        context = {'rental_info': rental_info}
    return render(request, 'rental_info.html', context)

# url /rent/vehicle/<pk> - show the specific vehicle also show whether it’s currently being rented
def vehicle_info(request, id): 
    vehicle_info = Vehicle.objects.get(id=id)
    context = {'vehicle_info': vehicle_info}
    return render(request, 'vehicle_info.html', context)

