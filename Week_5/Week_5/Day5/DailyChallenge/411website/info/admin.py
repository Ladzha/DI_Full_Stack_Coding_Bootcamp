from django.contrib import admin
from .models import Person, PersonAdmin
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.contrib.admin.widgets import AdminTextInputWidget



# class PhoneRegion(admin.ModelAdmin):
#     list_display = ['name', 'phone_number', 'email', 'address']
#     list_editable = ['phone_number']

#     formfield_overrides = {
#         PhoneNumberField: {"widget": PhoneNumberPrefixWidget},
#     }

#     search_fields = ('name', 'phone_number', 'email')
    
# admin.site.register(Person, PersonAdmin)


    
