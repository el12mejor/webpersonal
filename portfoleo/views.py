from django.shortcuts import render
from .models import Project
# Create your views here.
def portfoleo(request):
    projects = Project.objects.all()
    return render(request, 'portfoleo/portfoleo.html',{
        'project': projects
    })    
