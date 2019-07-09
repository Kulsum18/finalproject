from django.urls import path
from . import views

urlpatterns = [
    path('', views.tentangkami_index, name='tentangkami_index')
]