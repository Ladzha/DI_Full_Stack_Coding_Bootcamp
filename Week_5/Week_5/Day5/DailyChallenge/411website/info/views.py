from django.shortcuts import render, redirect
from .models import Person
from django.http import HttpResponse
from .forms import SearchForm

# Create your views here.

def by_phonenumber(request, number: str):
    try:
        about_person = Person.objects.get(phone_number=number)
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

# def search(request):     
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             number = form.cleaned_data.get('number')
#             if number:
#                 return redirect('number', phonenumber=number)
#             elif name:
#                 return redirect('name', name=name)
#         else:
#             print('OOOO')
#             return redirect('searchperson')
                
#     else:
#         form = SearchForm()
        
#     context = {'form': form}
#     return render(request, 'about_person.html', context )

def search(request):
    
    if request.method == 'POST':
        query = request.POST['search']

        if SearchForm({'number' : query}).is_valid():
            return redirect('phone', number = query)
        else:
            return redirect('name', name = query)

    return render(request, 'search.html')
