from django.shortcuts import render

# Create your views here.
def pendaftaranmember_index(request):
    return render(request, 'pendaftaranmember_index.html')
