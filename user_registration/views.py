from django.shortcuts import render, redirect
from django.contrib.auth import login
from user_registration.forms import RegistrationForm
from user_registration.models import RegistrationData

# Create your views here.


def user_reg(request):
    context = {
        "form": RegistrationForm,
    }
    return render(request, 'registration.html', context)


def addUser(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = RegistrationData(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                nama_lengkap=form.cleaned_data['nama_lengkap'],
                tgl_lahir=form.cleaned_data['tgl_lahir'],
                jenis_kelamin=form.cleaned_data['jenis_kelamin'],
                alamat=form.cleaned_data['alamat'],
                email=form.cleaned_data['email'],
                no_hp=form.cleaned_data['no_hp'],
                id_instagram=form.cleaned_data['id_instagram'],
                fb_url=form.cleaned_data['fb_url'],
                web_portofolio_url=form.cleaned_data['web_portofolio_url'],
                pekerjaan=form.cleaned_data['pekerjaan'],
                bidang_desain=form.cleaned_data['bidang_desain'],
                program_desain=form.cleaned_data['program_desain'],
                deskripsi_diri=form.cleaned_data['deskripsi_diri'],
                tujuan_gabung_bogrades=form.cleaned_data['tujuan_gabung_bogrades'],
                harapan_gabung_bogrades=form.cleaned_data['harapan_gabung_bogrades'],
                upload_foto_diri=form.cleaned_data['upload_foto_diri'],
                upload_portofolio=form.cleaned_data['upload_portofolio']

            )
            user.save()

            return redirect('registration')
