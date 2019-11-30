from django.db import models
class new_sighting (models.Model):
    
    Latitude = models.DecimalField(max_digits=8, decimal_places=6,blank=True,null=True)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6,blank=True,null=True)
    Unique_Squirrel_ID = models.CharField(max_length=50,blank=True,null=True)
    #Not required in the problem, but I think this field is necessary to form the unique id
    Hectare=models.CharField(max_length=3,blank=True,null=True) 
    
    PM='PM'
    AM='AM'
    shift_choices=[(PM,'PM'),(AM,'AM')]
    Shift=models.CharField(max_length=2,choices=shift_choices,blank=True,null=True)
    
    Date= models.DateField(blank=True,null=True)

    #Not required in the problem, but I think this field is necessary to form the unique id
    Hectare_Squirrel_Number=models.IntegerField(blank=True,null=True)
    
    adult='Adult'
    juvenile='Juvenile'
    age_choices=[(adult,'Adult'),(juvenile,'Juvenile')]
    Age=models.CharField(max_length=20,choices=age_choices,blank=True,null=True)
    
    grey='Grey'
    cinnamon='Cinnamon'
    black='Black'
    color_choices=[(grey,'Grey'), (cinnamon,'Cinnamon'), (black,'Black')]
    Primary_Fur_Color=models.CharField(max_length=20,choices=color_choices,blank=True,null=True) 
    
    Ground_Plane='Ground Plane'
    Above_Ground='Above_Ground'
    location_choices=[(Ground_Plane,'Ground Plane'),(Above_Ground,'Above_Ground')]
    Location=models.CharField(max_length=20,choices=location_choices,blank=True,null=True) 
    
    Specific_Location= models.CharField(max_length=50,blank=True,null=True)
    Running = models.BooleanField(blank=True,null=True)
    Chasing=models.BooleanField(blank=True,null=True)
    Climbing=models.BooleanField(blank=True,null=True)
    Eating=models.BooleanField(blank=True,null=True)
    Foraging=models.BooleanField(blank=True,null=True)
    Other_Activities=models.CharField(max_length=50,blank=True,null=True)
    #maybe we need to create a relation beetween these fiels, if one is true then the other 2 must be fasle. 
    Kuks=models.BooleanField(blank=True,null=True)
    Quaas=models.BooleanField(blank=True,null=True)
    Moans=models.BooleanField(blank=True,null=True)
    Tail_flags=models.BooleanField(blank=True,null=True)
    Tail_twitches=models.BooleanField(blank=True,null=True)
    Approaches=models.BooleanField(blank=True,null=True)
    Indifferent=models.BooleanField(blank=True,null=True)
    Runs_from=models.BooleanField(blank=True,null=True)
