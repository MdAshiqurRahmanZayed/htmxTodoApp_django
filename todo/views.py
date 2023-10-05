from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from todo.models import *

def todos(request):
    todos = Todo.objects.all()
    return render(request, 'base.html', {'todos': todos})

def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)
    
    return render(request, 'partials/todo.html', {'todo': todo})

def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title', '')
        todo.save()

        return render(request, 'partials/todo.html', {'todo': todo})
    
    return render(request, 'partials/edit.html', {'todo': todo})

def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.is_done:
          todo.is_done = False
    else:
          todo.is_done = True
         
    todo.save()

    return render(request, 'partials/todo.html', {'todo': todo})

def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()