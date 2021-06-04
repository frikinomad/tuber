from django.db import models

# Create your models here.
# we will have to put this model into admin.py - refer admin.py file
#this model will be used to control the information in the slider/carousel

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=120)
    fb_link = models.CharField(max_length=120)
    insta_link = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='media/team/%Y/%m/', null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name  #this will displayed in admin panel


class Slider(models.Model):
    headline = models.CharField(max_length=255) #we can write ( , black=True) to allow it to be blank
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/', null=True)    #/%Y/%m will create a folder with year and month name
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline     #this will be displayed in admin panel once we save a event description
