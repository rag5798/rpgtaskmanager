from django.shortcuts import render

def home(request):
    return render(
        request,
        "sidequest/index.html"
    )

def task(request):
    return render(
        request,
        "sidequest/task.html"
    )