from django.shortcuts import render, get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)      #to use get_object_or_404 we need to import it
    data = {
        'tuber': tuber,         #with this tuber we don't need to loop over it, this tuber will contain info of one youtuber only which is given by the pk
    }
    return render(request, 'youtubers/youtuber_detail.html', data) 


def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()      #this gives distinct values in terms of array since we used value_list
    #flat is flat type array i.e. normal type array
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    #imp code to filter according to kewyword
    if 'keyword' in request.GET:            #to check if there is a form input with name of keyword (check serch.html we have given the form name as keyword)
        keyword = request.GET['keyword']    #to receive the word that user has sent in this case 'keyword' and store it in a variable names keyword (ik a little confusing)
        if keyword:                         #again if keyword is true then filter and change tubers
            tubers = tubers.filter(description__icontains=keyword)      #icontain(if contains) comes from documentation, read https://docs.djangoproject.com/en/3.1/ref/models/querysets/
    #if we need to filter out using other clauses like name and all, we can use that as well, in place of description use that

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(city__iexact=category)

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/search.html', data) 
