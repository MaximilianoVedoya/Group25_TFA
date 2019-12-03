from django.core.management.base import BaseCommand, CommandError
from django.db import models
from sightings.models import new_sighting
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'export a csv file to the given path'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(str(options['path']),'w+') as csv_file:
            next(csv_file)
            squirrels=csv.reader(csv_file)

    def _write_csv(self, squirrels):
        writer = csv.writer(squirrels, encoding='utf-8')
        for squirrel in squirrels:
            s =squirrel[5]
            row = [unicode(getattr(obj, field)) for field in s]
            writer.writerow(row)
        
        f.close()
