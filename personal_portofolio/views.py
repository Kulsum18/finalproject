from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from projects.models import Portofolio
from blog.models import Post
from galerifoto.models import GaleriPost
from bogrades_shop.models import Product
from bogrades_shop.models import Category
from django.views.generic import View

def index(request):
    projects = Portofolio.objects.all()
    posts = Post.objects.all()
    galeriposts = GaleriPost.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'posts': posts,
        'galeriposts': galeriposts,
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def base_layout(request):
    template='personal_portofolio/base.html'
    return render(request, template)
