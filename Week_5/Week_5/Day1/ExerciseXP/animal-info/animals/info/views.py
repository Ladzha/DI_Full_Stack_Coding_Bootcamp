from django.shortcuts import render
from django.http import HttpResponse
import json
import os

# Create your views here.

json_file = os.path.dirname(os.path.realpath(__file__))
f = open (json_file+"\\" +'data_animals.json', "r")
data = json.loads(f.read())
animals = data['animals']
families = data['families']

def family(request,id):  
    family_selected = ''
    for i in families: 
        if i['id']==id:        
            family_selected == i 
    return render(request, 'family.html', family_selected)

def animal(request, id):
    animal_selected = ''
    for i in animals: 
        if i['id']==id:        
            animal_selected = i
    return render(request, 'animal.html', animal_selected)
