from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting
from .forms import new_sighting_form 
import random as random
from django.views.generic import ListView


def home_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    o_length=new_sighting.objects.count()
    squirrels_month={i: 0 for i in range(1,13)}

    # if the data is larger than 100, chose 100 random poitns, otherwise the server fries. 
    if o_length>100:
        length=[random.randint(1,o_length) for i in range(100)]
    else:
         length=[i for i in range(1,o_length)]

    # Creates a list with the number of sightings detected per month 
    for m in range (1,13):
        for i in length:
                if obj[i]["Date"].month == m:
                    squirrels_month[m]+=1
    list_squirrels=[squirrels_month[i] for i in range(1,13)]

    
    #creates a list that counts the number of squirrels by color
    color_={'Gray':0,'Cinnamon':0,'Black':0}

    for squirrel_color in ['Gray','Cinnamon','Black']:
        for i in length:
            if obj[i]["Primary_Fur_Color"] == squirrel_color:
                color_[squirrel_color]+=1
    primary_color=[color_[i] for i in ['Gray','Cinnamon','Black']]
    
  
    shift_={"AM":0, "PM":0}
    for shift in ["AM","PM"]:
        for i in length:
            if obj[i]["Shift"]== shift:
                shift_[shift]+=1
    
    Shift=[shift_[i] for i in ["AM","PM"]]
    
    info={
        "siquirrel_month": list_squirrels,
        "primary_color": primary_color,
        "Shift":Shift

    }
    return render(request,"home.html",info)
    
def map_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    o_length=new_sighting.objects.count()


    # if the data is larger than 100, chose 100 random poitns, otherwise the server fries. 
    if o_length>100:
        length=[random.randint(1,o_length) for i in range(100)]
    else:
         length=[i for i in range(1,o_length)]
    
    location=[(obj[i]['Latitude'],obj[i]['Longitude']) for i in length]
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
    if length>100:
        length=100
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

class DataList (ListView):
    model = new_sighting
    template_name= "data.html"
    paginate_by=100


    