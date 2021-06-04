from django.shortcuts import render,  get_object_or_404
from .models import Slider, Team
from youtubers.models import Youtuber
from datetime import date
# Create your views here.

def home(request):
    sliders = Slider.objects.all()  #this is similar to a mysql query, instead of all we can use order_by or anything else
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)  #this is coming from youtubers app, above sliders and teams are from webpages app
    latest_youtubers = Youtuber.objects.order_by('-created_date')       #in this created date and above we have written a minus(-) sign before date to signify in reverse order
    
    #to make the images clickable
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'latest_youtubers': latest_youtubers,
    }
    
    return render(request, 'webpages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
