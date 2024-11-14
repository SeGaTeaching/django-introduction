from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.index, name='index'),
    path('walter/', views.walter, name='walter'),
    path('math/<num1>/<num2>', views.math, name='math'),
]