from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, "core/contact.html")

def home(request):
    return render(request, "core/home.html")

