from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting
from .forms import new_sighting_form 

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
    
def map_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    
    length=new_sighting.objects.count()
    if length>100:
        length=100

    location=[(obj[i]['Latitude'],obj[i]['Longitude']) for i in range(length)]

    squirrel_location={
        "Location" : location,
        
    }
    return render(request,"map.html",squirrel_location)

def add_view(request, *args,**kwargs):
    form= new_sighting_form(request.POST or None)
    if form.is_valid():
        form.save()
        form=new_sighting_form()
    context={
        'form':form
    }
    return render(request,"add.html",context)

def sightings_view(request):
    return render(request,"sightings.html",{})

