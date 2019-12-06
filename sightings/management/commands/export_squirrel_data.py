from django.core.management.base import BaseCommand, CommandError
from django.db import models
from sightings.models import new_sighting
from datetime import datetime
import csv
import sys

class Command(BaseCommand):

    help = 'writes a csv file into some path that user inputs'
    def add_arguments(self, parser):
          parser.add_argument('path', type=str)

    def handle(self, *app_labels, **options):
        with open(str(options['path'])+'/file.csv','w',newline='') as f:
            fieldnames=['Longitude', 'Latitude','Unique_Squirrel_ID', 'Shift', 'Date','Age','Primary_Fur_Color'
            ,'Location','Specific_Location','Running','Chasing', 'Climbing','Eating' ,'Foraging',
            'Other_Activities' , 'Kuks','Quaas', 'Moans', 'Tail_flags', 'Tail_twitches', 'Approaches', 'Indifferent', 
            'Runs_from']
            thewriter=csv.DictWriter(f,fieldnames=fieldnames)
            thewriter.writeheader()

            squirrels= new_sighting.objects.values()
            rows =new_sighting.objects.count()
            
            for row in range(rows):
                thewriter.writerow({
            
                    'Longitude': squirrels[row]['Longitude'],
                    'Latitude': squirrels[row]['Latitude'],
                    'Unique_Squirrel_ID': squirrels[row]['Unique_Squirrel_ID'], 
                    'Shift': squirrels[row]['Shift'], 
                    'Date': squirrels[row]['Date'],
                    'Age': squirrels[row]['Age'],
                    'Primary_Fur_Color': squirrels[row]['Primary_Fur_Color'],
                    'Location': squirrels[row]['Location'],
                    'Specific_Location': squirrels[row]['Specific_Location'],
                    'Running': squirrels[row]['Running'],
                    'Chasing': squirrels[row]['Chasing'],
                    'Climbing': squirrels[row]['Climbing'],
                    'Eating': squirrels[row]['Eating'] ,
                    'Foraging': squirrels[row]['Foraging'],
                    'Other_Activities': squirrels[row]['Other_Activities'],
                    'Kuks': squirrels[row]['Kuks'],
                    'Quaas': squirrels[row]['Quaas'], 
                    'Moans': squirrels[row]['Moans'], 
                    'Tail_flags': squirrels[row]['Tail_flags'],
                    'Tail_twitches': squirrels[row]['Tail_twitches'], 
                    'Approaches': squirrels[row]['Approaches'], 
                    'Indifferent': squirrels[row]['Indifferent'], 
                    'Runs_from': squirrels[row]['Runs_from'],
                    })

        
            
        
        
        
        # sightings, new_sighting = app_labels[0].split('.')
        # model= get_model(sightings, new_sighting)
        
        # meta = {
        #     'file': str(options['path']),
        #     'class': new_sighting,
        #     'fields': ('Longitude', 'Latitude','Unique_Squirrel_ID', 'Hectare', 'Shift', 'Date', 'Hectare_Squirrel_Number', 'Age', 
        #             'Primary_Fur_Color','Location','Specific_Location','Running','Chasing', 'Climbing','Eating' ,'Foraging','Other_Activities' , 'Kuks','Quaas', 'Moans', 'Tail_flags', 'Tail_twitches', 'Approaches', 'Indifferent', ' Runs_from')

        # }
        # # self._write_csv(meta)
        
        # f = open(meta['file'], 'w+')
        # writer = csv.writer(f, encoding='utf-8')
        # writer.writerow( meta['fields'] )
        # for obj in meta['class'].objects.all():
        #     row = [unicode(getattr(obj, field)) for field in meta['fields']]
        #     writer.writerow(row)
        # f.close()