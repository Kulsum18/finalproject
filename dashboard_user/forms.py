from django import forms

class uploadImage(forms.Form):
    upload_foto_diri = forms.ImageField(upload_to="photoprofile/", null=True)
    upload_portofolio = forms.ImageField(upload_to="portofolio/", null=True)