from django.contrib import admin
from .models import AccountData

# Register your models here.
class AccountMemberAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccountData, AccountMemberAdmin)