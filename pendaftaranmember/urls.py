from django.urls import path
from . import views

urlpatterns = [
    path('', views.pendaftaranmember_index, name='pendaftaranmember_index')
]