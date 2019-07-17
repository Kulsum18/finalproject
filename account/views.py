from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AccountForm
from .models import AccountData

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user = AccountData(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    tgl_lahir = form.cleaned_data['tgl_lahir'],
                    jenis_kelamin = form.cleaned_data['jenis_kelamin'],
                    alamat = form.cleaned_data['alamat'],
                    phone_number = form.cleaned_data['phone_number'],
                    id_instagram = form.cleaned_data['id_instagram'],
                    fb_url = form.cleaned_data['fb_url'],
                    web_portofolio_url = form.cleaned_data['web_portofolio_url'],
                    pekerjaan = form.cleaned_data['pekerjaan'],
                    program_desain = form.cleaned_data['program_desain'],
                    deskripsi_diri = form.cleaned_data['deskripsi_diri'],
                    tujuan_gabung_bogrades = form.cleaned_data['tujuan_gabung_bogrades'],
                    harapan_gabung_bogrades = form.cleaned_data['harapan_gabung_bogrades']        
                )
        
                # user.upload_foto_diri = form.cleaned_data['upload_foto_diri']
                # user.upload_portofolio = form.cleaned_data['upload_portofolio']
                user.save()
               
                # Login the user
                # login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('register')

   # No post data availabe, let's just show the page.
    else:
        form = AccountForm()

    return render(request, template, {'form': form})