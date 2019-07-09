from django.shortcuts import render

# Create your views here.
def tentangkami_index(request):
    return render(request, 'index_tentangkami.html')
