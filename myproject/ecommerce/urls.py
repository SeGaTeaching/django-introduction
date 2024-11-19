from django.urls import path
from . import views
from .models import Customer, Product

urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.simple, name='simple'),
]