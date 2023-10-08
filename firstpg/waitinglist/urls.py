from django.urls import path
from . import views
from .views import ArtisanRegistrationView,ContactusRegistrationView,errorpg

from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static



app_name = 'waitinglist'

urlpatterns = [
    path("add/", ArtisanRegistrationView, name="add"),
    path("contact-us/", ContactusRegistrationView, name="contactus"),
    path("page_under_construction/", views.errorpg, name="error_page"),
    
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)