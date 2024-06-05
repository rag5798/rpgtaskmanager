import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(
        request,
        template_name="test_app/index.html"
    )

def hello_there(request, name):
    return render(
        request,
        'test_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def task(request):
    return render(
        request,
        "test_app/task.html"
    )