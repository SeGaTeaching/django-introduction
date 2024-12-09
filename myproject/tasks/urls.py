from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('add_task/', views.add_task, name='add_task'),
]
