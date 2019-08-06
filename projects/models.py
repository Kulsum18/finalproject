from django.db import models

# Create your models here.
class Portofolio(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Portofolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portofolio/")
    deskripsi_project = models.CharField(max_length=50, blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s ' % (self.post, self.image)

class ImageProfile(models.Model):
    username = models.CharField(max_length=100)
    profileimage = models.ImageField(upload_to="photoprofile/")
    def __str__(self):
        return self.username
