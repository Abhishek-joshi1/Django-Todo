from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['tasks']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')