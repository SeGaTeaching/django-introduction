from django.urls import path
from . import views

app_name = 'dtl'
urlpatterns = [
    path('', views.index, name='index'),
    path('filters/', views.filters, name='filters'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),

]
