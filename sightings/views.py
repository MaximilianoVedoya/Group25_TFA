from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    age_={'Adult':0, 'Juvenile':0}

    for squirrel_age in ['Adult','Juvenile']:
        for i in length:
            if obj[i]["Age"] == squirrel_age:
                age_[squirrel_age]+=1
    Age=[age_[i] for i in ['Adult','Juvenile']]
    
    #creates a pie chart of sightings by shift  
    shift_={"AM":0, "PM":0}
    for shift in ["AM","PM"]:
        for i in length:
            if obj[i]["Shift"]== shift:
                shift_[shift]+=1
    
    Shift=[shift_[i] for i in ["AM","PM"]]

    info={
        "siquirrel_month": list_squirrels,
        "primary_color": primary_color,
        "Age": Age,
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

def update_view(request, Unique_Squirrel_ID):
    instance = new_sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    form = new_sighting_form(request.POST or None, instance=instance)
    print(request.method)
    if form.is_valid() and request.method=="POST" :
          form.save()
    return render(request, 'update.html', {'form': form})
   

def delete_view(request, Unique_Squirrel_ID):
    template='delete.html'
    info= get_object_or_404(new_sighting,Unique_Squirrel_ID=Unique_Squirrel_ID)

    try:
        if request.methdod == "POST":
            form=new_sighting_form(request.POST,instance=info)
            info.delete()
            messages.success(request,'You have delete the record, that squirrrel is sad now')
        else:
            form=new_sighting_form(instance=info)
    except Exception as e:
        messages.warning(request,'the record could not be deleted: Error{}'.format(e))
    context={
        'form':form 
    }
    return render (request,template,context)

    
    
    
 
 
 
    # instance = new_sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    # form = new_sighting_form(request.POST or None, instance=instance)
    # if form.is_valid():
    #       form.delete()
    #     #   return redirect()
    # return render(request, 'delete.html', {'form': form})
    
    
    
    
    # obj=new_sighting.objects.values()
    # obj.delete()
    # return render(request, 'delete.html', {'form': form})