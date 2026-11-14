from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm, TaskStatusForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'app/project_list.html', {'projects': projects})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'app/project_form.html', {'form': form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()

    # Search & filter (requirement #6)
    query = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if query:
        tasks = tasks.filter(title__icontains=query) | tasks.filter(description__icontains=query)
    if status:
        tasks = tasks.filter(status=status)

    status_choices = Task.Status.choices
    return render(request, 'app/project_detail.html', {
        'project': project,
        'tasks': tasks,
        'query': query,
        'selected_status': status,
        'status_choices': status_choices,
    })


def task_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # assign the project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'app/task_form.html', {'form': form, 'project': project})


def task_update_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    return redirect('project_detail', pk=task.project.pk)


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        project_pk = task.project.pk
        task.delete()
        return redirect('project_detail', pk=project_pk)
    return render(request, 'app/task_confirm_delete.html', {'task': task})