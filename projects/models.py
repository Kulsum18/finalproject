from django.db import models

# Create your models here.
class Portofolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portofolio/")

    def __str__(self):
        return self.title

class ImageProfile(models.Model):
    username = models.CharField(max_length=100)
    profileimage = models.ImageField(upload_to="photoprofile/")
    def __str__(self):
        return self.username
