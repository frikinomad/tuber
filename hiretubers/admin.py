from django.contrib import admin
from .models import Hiretuber
# Register your models here.


class HiretuberAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'tuber_name', 'email')
    


admin.site.register(Hiretuber, HiretuberAdmin)