from django.shortcuts import render
from .models import Person
from django.http import HttpResponse

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


# def by_name(request, name_search: str):
#     person = None
#     try:
#         person = Person.objects.get(name=name_search)
#     except Person.DoesNotExist:
#         pass
#     context = {'person': person}
#     return render(request, 'search.html', context)