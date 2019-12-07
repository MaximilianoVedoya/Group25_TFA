# from django.db import models
# class new_sighting (models.Model):
    
#     Latitude = models.DecimalField(max_digits=5, decimal_places=3)
#     Longitude = models.DecimalField(max_digits=5, decimal_places=3)
#     Unique_Squirrel_ID = models.CharField(max_length=50,unique=True)
#     #Not required in the problem, but we think this field is necessary to form the unique id
#     Hectare=models.CharField(max_length=3,blank=True,null=True) 
    
#     PM='PM'
#     AM='AM'
#     shift_choices=[(PM,'PM'),(AM,'AM')]
#     Shift=models.CharField(max_length=2,choices=shift_choices)
    
#     Date= models.DateField()
#     #Not required in the problem, but we think this field is necessary to form the unique id
#     Hectare_Squirrel_Number=models.IntegerField(blank=True,null=True)
    
#     adult='Adult'
#     juvenile='Juvenile'
#     age_choices=[(adult,'Adult'),(juvenile,'Juvenile')]
#     Age=models.CharField(max_length=20,choices=age_choices,blank=True,null=True)
    
#     grey='Grey'
#     cinnamon='Cinnamon'
#     black='Black'
#     color_choices=[(grey,'Grey'), (cinnamon,'Cinnamon'), (black,'Black')]
#     Primary_Fur_Color=models.CharField(max_length=20,choices=color_choices,blank=True,null=True) 
    
#     Ground_Plane='Ground Plane'
#     Above_Ground='Above_Ground'
#     location_choices=[(Ground_Plane,'Ground Plane'),(Above_Ground,'Above_Ground')]
#     Location=models.CharField(max_length=20,choices=location_choices,blank=True,null=True) 
#     Specific_Location= models.CharField(max_length=50,blank=True,null=True)
#     Running = models.BooleanField()
#     Chasing=models.BooleanField()
#     Climbing=models.BooleanField()
#     Eating=models.BooleanField()
#     Foraging=models.BooleanField()
#     Other_Activities=models.CharField(max_length=50,blank=True,null=True)
    
#     Kuks=models.BooleanField()
#     Quaas=models.BooleanField()
#     Moans=models.BooleanField()
#     Tail_flags=models.BooleanField()
#     Tail_twitches=models.BooleanField()
#     Approaches=models.BooleanField()
#     Indifferent=models.BooleanField()
#     Runs_from=models.BooleanField()
