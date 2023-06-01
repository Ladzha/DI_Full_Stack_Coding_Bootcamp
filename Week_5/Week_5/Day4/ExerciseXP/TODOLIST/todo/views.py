from django.shortcuts import render
from .models import Todo, Category
from .forms import TodoForm, CategoryForm, DoneForm
from datetime import date


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
    if request.method =='POST':
        pass
    # todos_all = Todo.objects.all()
    done_form = DoneForm()
    category_all = Category.objects.all()
    context = {'category_list': category_all, 'done_form': done_form}
    return render(request, 'display_todos.html', context)
    # context = {'todo_list': todos_all, 'category_list': category_all}
    # return render(request, 'display_todos.html', context)
    
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