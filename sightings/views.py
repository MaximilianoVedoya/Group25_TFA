from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting
from .forms import new_sighting_form 
import json

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
    
def map_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    length=new_sighting.objects.count()
    if length>100:
        length=100
    location=[(obj[i]['Latitude'],obj[i]['Longitude']) for i in range(length)]
    squirrel_location={"Location" : location}
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
    obj=new_sighting.objects.values()
    length=new_sighting.objects.count()
    squirrel= [
        (   obj[i]['Latitude'],
            obj[i]['Longitude'],
            obj[i]['Unique_Squirrel_ID'],
            obj[i]['Hectare'],
            obj[i]['Shift'],
            obj[i]['Date'],
            obj[i]['Hectare_Squirrel_Number'],
            obj[i]['Age'],
            obj[i]['Primary_Fur_Color'],
            obj[i]['Location'],
            obj[i]['Specific_Location'],
            obj[i]['Running'],
            obj[i]['Chasing'],
            obj[i]['Climbing'],
            obj[i]['Eating'],
            obj[i]['Foraging'],
            obj[i]['Other_Activities'],
            obj[i]['Kuks'],
            obj[i]['Quaas'],
            obj[i]['Moans'],
            obj[i]['Tail_flags'],
            obj[i]['Tail_twitches'],
            obj[i]['Approaches'],
            obj[i]['Indifferent'],
            obj[i]['Runs_from']
        ) for i in range(length)]
    squirrels= {'squirrel' : squirrel }
    return render(request,"sightings.html",squirrels)


def data_view(request):

    obj=new_sighting.objects.values()
    info=[{"Latitude":1,"Longitude":2,"ID":3},{"Latitude":3,"Longitude":4,"ID":4}]
    info=json.dumps(info)
    dic_={"info": obj}
    return render(request,"data.html",dic_)

  # Latitude=[obj[i]['Latitude'] for i in range(length)]
    # Longitude=[obj[i]['Longitude'] for i in range(length)]
    # Unique_Squirrel_ID= [obj[i]['Unique_Squirrel_ID'] for i in range(length)]
    # Hectare= [obj[i]['Hectare'] for i in range(length)]
    # Shift= [obj[i]['Shift'] for i in range(length)]
    # Date= [obj[i]['Date'] for i in range(length)]
    # Hectare_Squirrel_Number= [obj[i]['Hectare_Squirrel_Number'] for i in range(length)]
    # Age= [obj[i]['Age'] for i in range(length)]
    # Primary_Fur_Color= [obj[i]['Primary_Fur_Color'] for i in range(length)]
    # Location= [obj[i]['Location'] for i in range(length)]
    # Specific_Location= [obj[i]['Specific_Location'] for i in range(length)]
    # Running= [obj[i]['Running'] for i in range(length)]
    # Chasing= [obj[i]['Chasing'] for i in range(length)]
    # Climbing= [obj[i]['Climbing'] for i in range(length)]
    # Eating= [obj[i]['Eating'] for i in range(length)]
    # Foraging = [obj[i]['Foraging'] for i in range(length)]
    # Other_Activities= [obj[i]['Other_Activities'] for i in range(length)]
    # Kuks = [obj[i]['Kuks'] for i in range(length)]
    # Quaas= [obj[i]['Quaas'] for i in range(length)]
    # Moans = [obj[i]['Moans'] for i in range(length)]
    # Tail_flags = [obj[i]['Tail_flags'] for i in range(length)]
    # Tail_twitches = [obj[i]['Tail_twitches'] for i in range(length)]
    # Approaches = [obj[i]['Approaches'] for i in range(length)]
    # Indifferent = [obj[i]['Indifferent'] for i in range(length)]
    # Runs_from = [obj[i]['Runs_from'] for i in range(length)]




    # squirrels={
    #     "Latitude" : Latitude,
    #     "Longitude": Longitude,
    #     "Unique_Squirrel_ID": Unique_Squirrel_ID,
    #     'Hectare' : Hectare,
    #     'Shift': Shift,
    #     'Date': Date,
    #     'Hectare_Squirrel_Number':Hectare_Squirrel_Number,
    #     'Age': Age,
    #     'Primary_Fur_Color': Primary_Fur_Color,
    #     'Location': Location,
    #     'Specific_Location':Specific_Location,
    #     'Running':Running,
    #     'Chasing': Chasing,
    #     'Climbing':Climbing,
    #     'Eating': Eating,
    #     'Foraging': Foraging,
    #     'Other_Activities': Other_Activities,
    #     'Kuks':Kuks,
    #     'Quaas':Quaas,
    #     'Moans':Moans,
    #     'Tail_flags':Tail_flags,
    #     'Approaches':Approaches,
    #     'Indifferent':Indifferent,
    #     'Runs_from':Runs_from,

    # }
    