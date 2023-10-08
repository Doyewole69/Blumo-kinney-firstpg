from django.contrib import admin
from .models import Artisan, ContactMessage

# Register your models here.

admin.site.register(Artisan)
admin.site.register(ContactMessage)