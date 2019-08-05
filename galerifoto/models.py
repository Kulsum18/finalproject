from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_image(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Ukuran file terlalu besar, batas maksimal 2 MB")

class GaleriPost(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField('Image', upload_to="images/", validators=[validate_image])
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title+": " +str(self.image)

# class Photo(models.Model):
#     image = models.ForeignKey(GaleriPost, on_delete=models.CASCADE, related_name='images')        