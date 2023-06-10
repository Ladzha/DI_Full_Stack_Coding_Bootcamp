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
            'rental_date': forms.DateInput(attrs={'type': 'date'})
        }
        
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'})
        }
        
class AddVihicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }
