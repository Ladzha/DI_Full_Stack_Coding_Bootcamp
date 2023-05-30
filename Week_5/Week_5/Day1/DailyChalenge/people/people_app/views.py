from django.shortcuts import render

# Create your views here.
people = [
    {
    "id": 1,
    "name": "Bob Smith",
    "age": 35,
    "country": "USA"
    },
    {
    "id": 2,
    "name": "Martha Smith",
    "age": 60,
    "country": "USA"
    },
    {
    "id": 3,
    "name": "Fabio Alberto",
    "age": 18,
    "country": "Italy"
    },
    {
    "id": 4,
    "name": "Dietrich Stein",
    "age": 85,
    "country": "Germany"
    }
]

def people_view(request):
    prople_sorted = sorted(people, key=lambda person: person['age'])
    context = {'people_list': prople_sorted} 
    return render(request, 'people_list.html', context)


# def people_view(request):
#     def age_sorted(x):
#         return x['age'] 
#     sorted_people_list = sorted(people_list, key = age_sorted)
#     for person in sorted_people_list:
#         message = (f"{person['id']}, {person['name']}, {person['age']}, {person['country']}")
#     return render(request, 'people_list.html', message)


# def personinfo(request, id):
#     context = {'people':people} 
#     context['id']==id        
#     return render(request, 'person.html', context)

def person_view(request, id:int):
    person = None
    for p in people:
        if p['id']==id:
            person=p
            break
        
    context = {'person_instance':person} 
    return render(request, 'person.html', context)