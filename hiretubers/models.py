from django.db import models
from datetime import datetime


# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)       #user_id is given to each user when they login, and we are giving blank=true i.e. even if user is not logged in they can still use that functionality
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email
    