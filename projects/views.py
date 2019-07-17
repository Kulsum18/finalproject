from django.shortcuts import render
from projects.models import Portofolio

# Create your views here.
def project_index(request):
    projects = Portofolio.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Portofolio.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)

