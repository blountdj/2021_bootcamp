from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tags.all() # many-to-many relationship
    reviews = projectObject.reviews.all() # get all the children of the object, using the related_name field
    context = {'project': projectObject,
               'tags': tags,
               'reviews': reviews}
    return render(request, 'projects/single-project.html', context)

def createProject(request):
    form = ProjectForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES) # request.FILES is for images
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project) # pre-fills the form with the project details

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project) # instance is required so project is updated, not a new project created
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}

    return render(request, 'projects/project-form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete.html', context)

