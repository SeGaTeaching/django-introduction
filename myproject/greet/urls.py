from django.urls import path
from . import views

app_name = 'greet'
urlpatterns = [
    path('walter/', views.walter, name='walter'),
    path('<str:name>/', views.index, name='index'),
    path('math/<num1>/<num2>', views.math, name='math'),
]