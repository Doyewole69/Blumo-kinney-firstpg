from django.urls import path
from . import views
from .views import ArtisanRegistrationView

from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static



app_name = 'waitinglist'

urlpatterns = [
    path("add/", ArtisanRegistrationView, name="add"),
    
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)