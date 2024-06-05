from django.urls import path
from test_app import views

urlpatterns = [
    path("" , views.home),
    path("test_app/<name>", views.hello_there, name="hello_there"),
    path("task", views.task)
]