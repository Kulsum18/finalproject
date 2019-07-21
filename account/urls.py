from django.conf.urls import url
from . import views

urlpatterns = [
    url('^user_register', views.user_register, name='user_register'),
]