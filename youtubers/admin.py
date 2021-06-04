from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):

    def myphoto(self, objects):
        return format_html('<img src="{}" width="40" />'.format(objects.photo.url))

    list_display = ('id', 'name','myphoto', 'subs_count', 'is_featured', 'created_date')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type', 'created_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)    #we can make other fields editable as well, but requrire some changes to make name and all editable

# Register your models here.
admin.site.register(Youtuber, YtAdmin)