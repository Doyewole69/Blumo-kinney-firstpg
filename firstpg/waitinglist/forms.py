from django import forms
from django.conf import settings
from .models import Artisan
from .constants import GENDER_CHOICE, SERVICES_RENDERED

class ArtisanForm(forms.ModelForm):
    
    class Meta:
        model = Artisan
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'company_name',
            'services',
            'skills',
            'unlisted_skill',
            'phone_number',
            'address',
            'landmark',
            'prefered_location',
            'guarantor_fullname',
            'guarantor_phone_number',
            'artisan_passport',
            'guarantor_passport',
            
            ]
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)