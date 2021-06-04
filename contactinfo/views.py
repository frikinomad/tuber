from django.shortcuts import render
from .models import Contactinfo

# Create your views here.
print('laptop')

def contactinfo(request):
    cinfo = Contactinfo.objects.all()
    data = {
        'cinfo': cinfo,
    }

    return render(request, 'webpages/home.html', data)