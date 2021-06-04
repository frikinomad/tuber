from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    fb_link = models.CharField(max_length=254)
    youtube_link = models.CharField(max_length=254)
    twitter_link = models.CharField(max_length=254)
    instagram_link = models.CharField(max_length=254)

    def __str__(self):
        return self.email
    

