from django.db import models

# Create your models here.
class Portofolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/portofolio")

class ImageProfile(models.Model):
    username = models.CharField(max_length=100)
    profileimage = models.FilePathField(path="/photoprofile")    
