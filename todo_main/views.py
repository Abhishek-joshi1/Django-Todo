from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(isCompleted = False)
    print(tasks)
    context = {
        "tasks" : tasks,
    }
    return render(request, 'home.html', context)