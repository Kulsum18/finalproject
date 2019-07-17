from django.contrib import admin
from user_registration.models import RegistrationData

# Register your models here.
class UserRegistrationAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(RegistrationData, UserRegistrationAdmin)
