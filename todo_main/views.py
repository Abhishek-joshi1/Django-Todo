from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(isCompleted = False).order_by('-updatedAt')
    context = {
        "tasks" : tasks,
    }
    return render(request, 'home.html', context)