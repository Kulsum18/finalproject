from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard_user/', include('django.contrib.auth.urls')),
]