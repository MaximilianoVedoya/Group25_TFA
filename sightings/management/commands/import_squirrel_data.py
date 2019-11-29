from django.core.management.base import BaseCommand, CommandError
from django.db import models
from sightings.models import new_sighting
from datetime import datetime
import csv 
class Command(BaseCommand):
    help = 'reads a csv file into database'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(str(options['path']),'r') as csv_file:
            next(csv_file)
            squirrels=csv.reader(csv_file)
            
            #Function to translate the FALSE/TRUE from the table into keywords.
            def boolean_translator(i):
                if squirrel[i].upper()=="FALSE":
                    return(False)
                else:
                    return(True)
            
            for squirrel in squirrels:
                s=squirrel[5]#I use this variable to be able to parse the date form the database. 
                p=new_sighting(
                    Longitude=squirrel[0],
                    Latitude=squirrel[1],
                    Unique_Squirrel_ID =squirrel[2],
                    Hectare=squirrel[3],
                    Shift=squirrel[4],
                    Date=datetime(month=int(s[0:2]),day=int(s[2:4]),year=int(s[4:8])),#Here I use the variable "s"
                    Hectare_Squirrel_Number=squirrel[6],
                    Age=squirrel[7],
                    Primary_Fur_Color=squirrel[8],
                    Location=squirrel[12],
                    Specific_Location=squirrel[14],
                    Running =boolean_translator(15),
                    Chasing=boolean_translator(16),
                    Climbing=boolean_translator(17),
                    Eating=boolean_translator(18),
                    Foraging=boolean_translator(19),
                    Other_Activities=squirrel[20],
                    Kuks=boolean_translator(21),
                    Quaas=boolean_translator(22),
                    Moans=boolean_translator(23),
                    Tail_flags=boolean_translator(24),
                    Tail_twitches=boolean_translator(25),
                    Approaches=boolean_translator(26),
                    Indifferent=boolean_translator(27),
                    Runs_from=boolean_translator(28),
                )  
                p.save()
   
        
       