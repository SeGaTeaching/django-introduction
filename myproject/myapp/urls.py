from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('request/', views.show, name='show'),
    path('request/json/', views.heike),
    path('response/', views.answer),
    path('forms/', views.form, name='form'),
]
