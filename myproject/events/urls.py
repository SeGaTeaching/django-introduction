from django.urls import path
from . import views

urlpatterns = [
    path('', views.event, name='event'),
    path('success/<int:event_id>/', views.event_success, name='event_success'),
]