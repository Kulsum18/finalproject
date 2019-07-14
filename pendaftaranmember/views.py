from django.shortcuts import render
from pendaftaranmember.forms import RegistrationForm

# Create your views here.
def user_register(request):
    form = RegistrationForm
    context = { 
        "forms": form,
    }
    return render(request, 'registration.html', context)

    
