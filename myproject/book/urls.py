from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('django-form/', views.library_book, name='library_book'),
    #path('library_success/', views.library_book, name='library_book'),
]