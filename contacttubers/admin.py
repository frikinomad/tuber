from django.contrib import admin
from .models import Contacttuber
# Register your models here.

class ContacttuberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name')

admin.site.register(Contacttuber, ContacttuberAdmin)
