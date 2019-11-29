from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
    
def map_view(request, *args,**kwargs):

    return render(request,"map.html",{})

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})

def sightings_view(request):
    return render(request,"sightings.html",{})

