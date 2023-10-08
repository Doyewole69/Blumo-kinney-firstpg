from django.db import models
from .constants import GENDER_CHOICE, SERVICES_RENDERED
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Artisan(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25 , blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=False )
    email = models.EmailField(unique=True, null=False, blank=False )
    company_name = models.CharField(max_length=225)
    services = models.CharField(max_length=30, choices=SERVICES_RENDERED)
    skills = models.CharField(max_length=30, choices=SERVICES_RENDERED)
    unlisted_skill = models.CharField(max_length=225)
    phone_number = models.IntegerField(unique=True, blank=False)
    address = models.CharField(max_length=225, blank=False)
    landmark = models.CharField(max_length=25, )
    prefered_location = models.CharField(max_length=225)
    guarantor_fullname = models.CharField(max_length=225)
    guarantor_phone_number = models.IntegerField(unique=True, blank=False)
    artisan_passport = models.ImageField(upload_to = 'static/images/')
    guarantor_passport = models.ImageField(upload_to = 'static/images/')
    
    def __str__(self):
        return self.email
    
    
    
    
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number =models.IntegerField(blank=False)
    service_needed = models.CharField(max_length=200)
    special_request = models.TextField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_needed