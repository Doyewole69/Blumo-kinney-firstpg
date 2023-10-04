from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import ArtisanForm
from .models import Artisan


# Create your views here.



class HomeView(TemplateView):
    template_name = 'index.html'


def ArtisanRegistrationView(request):
    form = ArtisanForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if Artisan.objects.filter(email=instance.email).exists():
            print("Sorry! This email already exists")
        else:
            instance.save()

    context = {
        'form' : form,
    }
    template = 'artisanspage.html'
    return render(request, template, context)
   
    
   