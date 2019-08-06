from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    url(r'(?P<id>\d+)/portofolio_delete/$', views.portofolio_delete, name="portofolio_delete"),
    url(r'(?P<id>\d+)/portofolio_detail/$', views.portofolio_detail, name="portofolio_detail"),
]
