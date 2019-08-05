# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'jenis_kelamin', 'alamat', 'no_handphone', 'id_instagram', 'fb_url', 'web_portofolio_url', 'pekerjaan', 'program_desain', 'deskripsi_diri', 'tujuan_gabung_bogrades', 'harapan_gabung_bogrades']

admin.site.register(CustomUser, CustomUserAdmin)    
