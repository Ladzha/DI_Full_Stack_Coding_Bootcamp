from django.contrib import admin
from .models import Person
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.contrib.admin.widgets import AdminTextInputWidget

admin.site.register(Person)
# Register your models here.
