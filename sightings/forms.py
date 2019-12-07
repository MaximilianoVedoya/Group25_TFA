from django import forms 
from .models import new_sighting
import datetime

class new_sighting_form(forms.ModelForm):
    Date= forms.DateField(widget=forms.DateInput(attrs={"placeholder": datetime.datetime.now().strftime("%x")}))
    class Meta:
        model = new_sighting

        #Define each of fields associated with Squirrel sighting
        fields =[
            'Latitude', 
            'Longitude',
            'Unique_Squirrel_ID',
            'Shift',
            'Date',
            'Hectare',
            'Hectare_Squirrel_Number',
            'Age',
            'Primary_Fur_Color',
            'Location',
            'Specific_Location',
            'Running',
            'Chasing',
            'Climbing',
            'Eating',
            'Foraging',
            'Other_Activities',
            'Kuks',
            'Quaas',
            'Moans',
            'Tail_flags',
            'Tail_twitches',
            'Approaches',
            'Indifferent',
            'Runs_from'

        ]
