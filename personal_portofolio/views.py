from django.shortcuts import render
from projects.models import Project
from blog.models import Post

def index(request):
	projects = Project.objects.all()
	posts = Post.objects.all() 
	context = {
        'projects' : projects,
		'posts' : posts,
    }
	return render(request,'index.html', context)