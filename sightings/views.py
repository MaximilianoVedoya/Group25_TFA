from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
    
def map_view(request, *args,**kwargs):
    return render(request,"map.html",{})

def sightings_view(request, *args,**kwargs):
    return render(request,"sightings.html",{})

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})