from django.contrib import admin
from galerifoto.models import GaleriPost

class GaleriPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(GaleriPost, GaleriPostAdmin)
