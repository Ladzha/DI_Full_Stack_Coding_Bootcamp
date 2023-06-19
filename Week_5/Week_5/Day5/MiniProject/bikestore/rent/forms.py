from django import forms
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation, Address

class AddCustomerForm(forms.ModelForm):
    # field_name = forms.ChoiceField(**options)
    class Meta:
        model = Customer
        fields = '__all__'

class AddRentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
        widgets = {
            'rental_date': forms.DateInput(attrs={'type': 'date'}), 'return_date': forms.DateInput(attrs={'type': 'date'})
        }
        
        
class AddVihicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'real_cost', 'size']