from django.urls import path
from rent.views import *

urlpatterns = [
    path('rental/', all_rentals, name = 'all_rentals'),
    path('vehicle/', all_vehicles, name = 'all_vehicles'),
    path('customer/', all_customers, name = 'all_customers'),
    path('customer/add/', add_customer, name = 'add_customer'),
    path('rental/add/', add_rental, name = 'add_rental'),
    path('vehicle/add/', add_vehicle, name = 'add_vehicle'),
    path('customer/<int:id>', customer_info, name = 'customer_info'),
    path('rental/<int:id>', rental_info, name = 'rental_info'),
    path('vehicle/<int:id>', vehicle_info, name = 'vehicle_info'),
]