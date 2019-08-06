from django.contrib import admin
from .models import Portofolio, Image

# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class PortofolioAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        super(PortofolioAdmin,self).save_model(request, obj, form, change)
        # obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(image=afile)

admin.site.register(Portofolio, PortofolioAdmin)
