from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeri, name='galeri'),
    path('<int:pk>/', views.galeri_detail, name='galeri_detail'),
]