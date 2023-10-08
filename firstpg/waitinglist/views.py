from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ArtisanForm
from .models import Artisan, ContactMessage
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'index.html'

def ArtisanRegistrationView(request):
    if request.method == 'POST':
        form = ArtisanForm(request.POST , request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if an Artisan with the same email already exists
            if Artisan.objects.filter(email=email).exists():
                print("Sorry! This email already exists")
            else:
                form.save()  # Save the form data to the database
                return redirect('home')  # Redirect to a success page
    else:
        form = ArtisanForm()

    context = {
        'form': form,
    }
    template = 'artisanspage.html'
    return render(request, template, context)

def ContactusRegistrationView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a thank you page here
            return redirect('home')  # Replace 'thank_you' with the actual URL name
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def errorpg(request):
    return render(request, "errorpg.html", {})