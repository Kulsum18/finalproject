from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'jenis_kelamin', 'alamat', 'no_handphone', 'id_instagram', 'fb_url', 'web_portofolio_url', 'pekerjaan', 'program_desain', 'deskripsi_diri', 'tujuan_gabung_bogrades', 'harapan_gabung_bogrades')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'jenis_kelamin', 'alamat', 'no_handphone', 'id_instagram', 'fb_url', 'web_portofolio_url', 'pekerjaan', 'program_desain', 'deskripsi_diri', 'tujuan_gabung_bogrades', 'harapan_gabung_bogrades')        