# todo/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Todo

# Index view to display the to-do list
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# View to add a new to-do item
def add_todo(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todo_text')
        if todo_text:
            Todo.objects.create(text=todo_text)
            return redirect('index')
    return render(request, 'todo/add_todo.html')

# View to delete a to-do item
def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('index')
