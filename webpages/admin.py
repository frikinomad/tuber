from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html   #to display images


class TeamAdmin(admin.ModelAdmin):
    
    def myphoto(self, objects):
        return format_html('<img src="{}" width="40" />'.format(objects.photo.url))


    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')    #this shows all the given fields in panel, we can add more
    list_display_links = ('first_name',)        #this makes the first_name clickable in admin panel, we can add or remove more
    #above we are using a comma since lists cannot have a single value, it will give error
    search_fields = ('first_name', 'role')      #using this we can create our own search fields to filter through the values
    list_filter = ('role',)     #this gives filter option according to given value, we can use first_name instead of role to filter using first_name
    #above list are already there in django we are just overwriting them and passing the class function in the admin panel

class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, objects):
        return format_html('<img src="{}" height="40" width="40" />'.format(objects.photo.url))
    
    list_display = ('button_text', 'headline', 'myphoto')
    list_display_links = ('button_text',)


# Register your models here.
admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
