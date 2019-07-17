from django.contrib import admin
from galerifoto.models import GaleriPost

# Register your models here.
class GaleriPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(GaleriPost, GaleriPostAdmin)
