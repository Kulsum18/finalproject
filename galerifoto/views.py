from django.shortcuts import render
from galerifoto.models import GaleriPost

# Create your views here.
def galeri(request):
    galeriposts = GaleriPost.objects.all().order_by('-created_on')
    context = {
        'galeriposts' : galeriposts,
    }
    return render(request, 'galeri.html', context)

def galeri_detail(request, pk):
    galeripost = GaleriPost.objects.get(pk=pk)

    if request.method == 'POST':
        post = GaleriPost.objects.filter(post=post)
    context = {
        'galeripost': galeripost,
    }
    return render(request, 'galeri_detail.html', context)