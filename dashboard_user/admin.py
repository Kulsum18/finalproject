from django.contrib import admin
from .models import PostPortofolio, Images

# Register your models here.
class PostPortofolioAdmin(admin.ModelAdmin):
    list_display = ('nama_project', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    list_editable = ('status',)
    date_hierarchy = ('created')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(PostPortofolio, PostPortofolioAdmin)
admin.site.register(Images, ImagesAdmin)
