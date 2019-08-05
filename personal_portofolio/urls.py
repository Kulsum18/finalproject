"""personal_portofolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='main_index'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('tentangkami/', include("tentangkami.urls")),
    path('projects/', include("projects.urls")),
    path('galerifoto/', include("galerifoto.urls")),
    # path('account/', include("account.urls")),
    # path('dashboard_user', auth_views.LoginView, {'template_name': 'personal_portofolio/signin.html'}, name='login'),
    # path('login/', auth_views.LoginView, {'template_name': 'signin.html'}, name='login'),
    # path('logout/', auth_views.LogoutView, {'template_name': 'dashboarduser.html'}, name='logout'),
    path('blog/', include("blog.urls")),
    path('cart', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include("bogrades_shop.urls", namespace='bogrades_shop')),
    path('dashboard_user/', include("dashboard_user.urls", namespace='dashboard')),
    path('',include('pwa.urls')),
    # path('dashboard_user/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


