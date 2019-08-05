from django import forms

class uploadImage(forms.Form):
    upload_portofolio = forms.ImageField(upload_to="portofolio/", null=True)