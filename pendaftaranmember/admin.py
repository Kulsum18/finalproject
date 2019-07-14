from django.contrib import admin
from pendaftaranmember.models import PendaftaranMember


# Register your models here.
class PendaftaranMemberAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(PendaftaranMember)
