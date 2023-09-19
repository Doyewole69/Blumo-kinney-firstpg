from django import forms
from django.conf import settings
from models import Artisan
from .constants import GENDER_CHOICE, SERVICES_RENDERED

class ArtisanForm(forms.ModelForm):
    
    class Meta:
        model = Artisan
        fields = [
            
        ]