from django.shortcuts import render
from projects.models import Project

# Create your views here.


# view to show all prjects snippet
def project_index(request):
    projects = Project.objects.all()  # projects queryset
    context = {
        "projects": projects
    }
    return render(request, 'project_index.html', context)


# view to show particular project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, 'project_detail.html', context)
