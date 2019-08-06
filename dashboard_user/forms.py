from django import forms
from .models import PostPortofolio

class PostPortofolioCreateForm(forms.ModelForm):
    class Meta:
        model = PostPortofolio
        fields = (
            'nama_project',
            'author',
            'bidang_desain',
            'deskripsi_project',
            'status',
        )

class PostPortofolioEditForm(forms.ModelForm):
    class Meta:
        model = PostPortofolio
        fields = (
            'nama_project',
            'author',
            'bidang_desain',
            'deskripsi_project',
            'status',
        )