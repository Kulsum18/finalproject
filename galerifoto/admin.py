from django.contrib import admin
from galerifoto.models import GaleriPost

# Register your models here.
# class PhotoInline(admin.TabularInline):
#     model = Photo
#     extra = 2

class GaleriPostAdmin(admin.ModelAdmin):
    pass
    # inlines = [PhotoInline]

    # def save_model(self, request, obj, form, change):
    #     obj.save()

    #     for afile in request.FILES.getlist('photos_multiple'):
    #         obj.photos.create(image=afile)

admin.site.register(GaleriPost, GaleriPostAdmin)
