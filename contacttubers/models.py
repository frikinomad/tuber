from django.db import models
from datetime import datetime

# Create your models here.
class Contacttuber(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=False, default=datetime.now)

    def __str__(self):
        return self.company_name
    