from django.shortcuts import render
from .models import Project

# Create your views here.

def experiencia(request):
    return render(request, 'portfolio/experiencia.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {"projects": projects})
    