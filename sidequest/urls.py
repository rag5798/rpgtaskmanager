from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home, name='home'),
    path("task", views.task, name='task'),
    path('login', views.add_user, name='add_user'),
]