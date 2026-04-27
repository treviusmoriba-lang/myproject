from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>My First Hosted Website</h1><p>Running live from VS Code!</p>") 
