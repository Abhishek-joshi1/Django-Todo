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

def markAsUnDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = False
    task.save()
    return redirect('home') 

def Edit_Task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['tasks']
        get_task.task = new_task
        print(get_task)
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

def Delete_Task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')