from django.shortcuts import render, get_object_or_404, redirect
from .models import PostPortofolio, Images
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.forms import modelformset_factory
from django.contrib import messages

from .forms import *

# Create your views here.
# def dashboard(request):
    
#     return render(request, 'dashboarduser.html')
def member_bogrades(request):
    member_bogrades = PostPortofolio.published.all()
    query = request.GET.get('q')
    if query:
        member_bogrades = PostPortofolio.published.filter(
        Q(nama_project__icontains=query)|
        Q(deskripsi_project__icontains=query)
        )
    paginator = Paginator(portofolio_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'posts': posts,
        'page_range': page_range,
    }
    return render(request, 'member_bogrades.html', context)

def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

def dashboard(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=3)
    if request.method == 'POST':
        form = PostPortofolioCreateForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.save()
            print(formset.cleaned_data)
            for f in formset:
                print(f.cleaned_data)
                try:
                    photo = Images(post=post, image=f.cleaned_data.get('image'))
                    photo.save()
                except Exception as e:
                    break
            messages.success(request, "Post has been successfully created.")
            return redirect('member_bogrades')
    else:
        form = PostPortofolioCreateForm()
        formset = ImageFormset(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'dashboarduser.html', context)

def portofolio_detail(request, id):
    post = get_object_or_404(PostPortofolio, id=id, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'portofolio_detail.html', context)

def portofolio_delete(request, id):
    post = get_object_or_404(PostPortofolio, id=id)
    if request.user != post.author:
        raise Http404()
    post.delete()
    messages.warning(request, 'post has been successfully deleted!')
    return redirect('member_bogrades')   