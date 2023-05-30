from django.shortcuts import render
from.models import Animals, Family

# Create your views here.
def family(request, family_id):
    family_selected = Family.objects.get(id=family_id)
    animal_selected = Animals.objects.filter(family=family)
    return render(request, 'family.html', {'family': family_selected, 'animal': animal_selected})

def animal(request, id):
    animal_selected = Animals.objects.get(id=id)
    return render(request, 'animal.html', {'animal': animal_selected})

def animallist(request):
    animal_all = Animals.objects.all()
    context = {'animal_list': animal_all}

    return render(request, 'animallist.html', context)

# def person_view(request, id:int):
#     person = None
#     for p in people:
#         if p['id']==id:
#             person=p
#             break
        
#     context = {'person_instance':person} 
#     return render(request, 'person.html', context)