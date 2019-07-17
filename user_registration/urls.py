from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_reg, name='user_reg'),
    path('', views.addUser, name='addUser')
]