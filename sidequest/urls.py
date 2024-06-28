from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home, name='home'),
    path("task", views.task, name='task'),
    path("character_info", views.character, name='character_info')
]