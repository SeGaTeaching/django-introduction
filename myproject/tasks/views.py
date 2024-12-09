from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import TaskForm, AsyncTaskForm
from .models import Task

# Create your views here.
@login_required(login_url='accounts:login')
def tasks_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task = Task(title=title, user=request.user)
            task.save()
        tasks = Task.objects.filter(user=request.user)
        async_form = AsyncTaskForm()
        return render(request, 'tasks/tasks_list.html', {'form': form, 'tasks': tasks, 'async_form': async_form}) 
    else:
        form = TaskForm()
        async_form = AsyncTaskForm()
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks_list.html', {'form': form, 'tasks': tasks, 'async_form': async_form})

def add_task(request):
    if request.method == 'POST':
        async_form = AsyncTaskForm(request.POST)
        if async_form.is_valid():
            title = async_form.cleaned_data['title']
            task = Task(title=title, user=request.user)
            task.save()
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'created_at': task.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)

