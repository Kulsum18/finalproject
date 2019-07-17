from django.db import models

# Create your models here.
class GaleriPost(models.Model):
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description