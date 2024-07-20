from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("task", views.task, name='task'),
    path("character", views.character, name='character'),
    path('login', views.custom_login_view, name='login'),
    path('register', views.register, name='register'),
    path('task_creation/', views.task_creation, name='task_creation'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('character/select/', views.character_selection, name='character_select'),
    path('character_roll/<int:character_id>/', views.character_roll, name='character_roll'),
    path('battle/', views.battle_view, name='battle'),
    path('victory/', views.victory_view, name='victory'),
]