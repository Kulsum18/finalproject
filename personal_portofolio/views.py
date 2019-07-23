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

    # def login_request(request):
    #     form = AuthenticationForm()
    # return render(request=request,
    #               template_name="dashboarduser.html",
    #               context={"form": form})

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('dashboard_index')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "main_index")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
    
# def login(request):
#     username='not logged in'
#     if request.method == 'POST':
#         MyLoginForm = LoginForm(request.POST)
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#             request.session['username'] = username
#         else:
#             MyLoginForm = LoginForm()
#     return render(request, 'dashboarduser.html', {"username":username})

# def formView(request):
#     if request.session.has_key('username'):
#         username = request.session['username']
#         return render(request, 'dashboarduser.html', {"username":username})
#     else:
#         return render(request, 'signin.html', {})
        
# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("main_index")


# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request,
#                   template_name="login.html",
#                   context={"form": form})

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     if user.is_active:
    #         login(request, user)
    #         messages.info(request, "You are now logged in as {username}")
    #         return redirect('dashboard_user')
    #     else:
    #         messages.error(request, "Invalid username or password")


# def my_dashboard(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             messages.info(request, "You are now logged in as {username}")
#             return redirect('dashboard_user')
#         else:
#             messages.error(request, "Invalid username or password")
