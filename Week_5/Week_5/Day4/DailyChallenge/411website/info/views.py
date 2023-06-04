from django.shortcuts import render, redirect
from .models import Person
from django.http import HttpResponse
from .forms import SearchForm

# Create your views here.

def by_phonenumber(request, phonenumber: str):
    try:
        about_person = Person.objects.get(phone_number=phonenumber)
        context = {'info_list': about_person}
        return render(request, 'about_person.html', context)
    except:
        context = 'Person no exist'
        return HttpResponse(context, request)


def by_name(request, name: str):
    try:
        about_person = Person.objects.get(name=name)
        context = {'info_list': about_person}
        return render(request, 'about_person.html', context)
    except:
        context = 'Person no exist'
        return HttpResponse(context, request)

def search(request):     
    if request.method == 'POST':
        data = request.POST['search']

        if SearchForm({'number' : data}).is_valid():
            return redirect('phone_number', number = data)
        else:
            return redirect('name', input_name = data)

    return render(request, 'search.html')
