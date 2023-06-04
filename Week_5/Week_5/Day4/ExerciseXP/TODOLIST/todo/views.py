from django.shortcuts import render, redirect
from .models import Todo, Category
from .forms import TodoForm, CategoryForm, DoneForm
from datetime import date, datetime


# Create your views here.
def add_todo(request):
    #POST
    if request.method == 'POST':
        data = request.POST
        filled_form = TodoForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
    # GET
    todo_form = TodoForm()
    context = {'form': todo_form}
    return render(request, 'add_todo.html', context)

def add_category(request):
    #POST
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        if filled_form.is_valid():
            filled_form.save()
        else:
            print(filled_form.errors)
    # GET
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)


def display_todos(request):
    todos_all = Todo.objects.all()
    context = {'todos_all': todos_all}
    return render(request, 'display_todos.html', context)

def todo_done(request, id):
    task = Todo.objects.get(id=id)

    if request.method == "POST":
        if 'done' in request.POST:
            task.has_been_done = True
            task.date_completion = datetime.datetime.now()
            task.save()
        elif 'undone' in request.POST:
            task.has_been_done = False
            task.date_completion = None
            task.save()

    return redirect('display_todos')