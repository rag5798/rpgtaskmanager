from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("" , views.home, name='home'),
    path("task", views.task, name='task'),
    path('login/', views.custom_login_view, name='login'),
    path('register/', views.register, name='register'),
    path('task_creation/', views.task_creation, name='task_creation'),
]