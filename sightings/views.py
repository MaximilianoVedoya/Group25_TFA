from django.shortcuts import render
from django.http import HttpResponse
from .models import new_sighting
from .forms import new_sighting_form 
import random as random
from django.views.generic import ListView
from django.core.paginator import Paginator



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

     #creates a list that counts the number of squirrels by age
    age_={'Adult':0,'Juvenile':0}

    for squirrel_age in ['Adult','Juvenile']:
        for i in length:
            if obj[i]["Age"] == squirrel_age:
                age_[squirrel_age]+=1
    _Age=[age_[i] for i in ['Adult','Juvenile']]
    
  
    shift_={"AM":0, "PM":0}
    for shift in ["AM","PM"]:
        for i in length:
            if obj[i]["Shift"]== shift:
                shift_[shift]+=1
    
    Shift=[shift_[i] for i in ["AM","PM"]]

    info={
        "siquirrel_month": list_squirrels,
        "primary_color": primary_color,
        "Age": _Age,
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

def update_view(request, *args,**kwargs):
    #obj=new_sighting.objects.values()
    form= new_sighting_form(request.POST or None)
    if form.is_valid():
        form.save()
    context={
       # 'instance' :obj, 
        'form':form,
    }
    return render(request,"update.html",context)

def delete_view(request, *args,**kwargs):
    obj=new_sighting.objects.values()
    obj.delete()

def sightings_view(request):
    squirrel_list = new_sighting.objects.all()
    paginator = Paginator(squirrel_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    squirrels = paginator.get_page(page)
    return render(request, 'sightings.html', {'squirrels': squirrels})


def DataList(request):
    squirrel_list = new_sighting.objects.all()
    paginator = Paginator(squirrel_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    squirrels = paginator.get_page(page)
    return render(request, 'data.html', {'squirrels': squirrels})


    