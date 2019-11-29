from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
    
def map_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    length=new_sighting.objects.count()

    location=[(obj[i]['Latitude'],obj[i]['Longitude']) for i in range(length)]

    squirrel_location={
        "Location" : location,
        
    }
    return render(request,"map.html",squirrel_location)

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})

def sightings_view(request):
    return render(request,"sightings.html",{})

