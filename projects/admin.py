from django.contrib import admin
from .models import Portofolio, ImageProfile

# Register your models here.
class PortofolioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Portofolio, PortofolioAdmin)

class ImageProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImageProfile, ImageProfileAdmin)
