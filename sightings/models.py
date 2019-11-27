from django.db import models

class new_sighting (models.Model):
    PM='PM'
    AM='AM'
    shift_choices=[(PM,'PM'),(AM,'AM')]
    Shift=models.CharField(max_length=2,choices=shift_choices)
    Latitude = models.DecimalField(max_digits=8, decimal_places=3)
    Longitude = models.DecimalField(max_digits=8, decimal_places=3)
    Unique_Squirrel_ID = models.AutoField(primary_key=True)
    Date= models.DateField()
    adult='Adult'
    juvenile='Juvenile'
    age_choices=[(adult,'Adult'),(juvenile,'Juvenile')]
    Age=models.CharField(max_length=20,choices=age_choices)

    grey='Grey'
    cinnamon='Cinnamon'
    black='Black'
    color_choices=[(grey,'Grey'), (cinnamon,'Cinnamon'), (black,'Black')]
    Primary_Fur_Color=models.CharField(max_length=20,choices=color_choices) 

    Ground_Plane='Ground Plane'
    Above_Ground='Above_Ground'
    location_choices=[(Ground_Plane,'Ground Plane'),(Above_Ground,'Above_Ground')]
    Location=models.CharField(max_length=20,choices=location_choices) 
    Specific_Location= models.CharField(max_length=50)
    Running = models.BooleanField()
    Chasing=models.BooleanField()
    Climbing=models.BooleanField()
    Eating=models.BooleanField()
    Foraging=models.BooleanField()
    Other_Activities=models.CharField(max_length=50)
    #maybe we need to create a relation beetween these fiels, if one is true then the other 2 must be fasle. 
    Kuks=models.BooleanField()
    Quaas=models.BooleanField()
    Moans=models.BooleanField()
    Tail_flags=models.BooleanField()
    Tail_twitches=models.BooleanField()
    Approaches=models.BooleanField()
    Indifferent=models.BooleanField()
    Runs_from=models.BooleanField()
