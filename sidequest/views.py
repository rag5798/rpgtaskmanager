from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserDataForm
from .models import UserData

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

def login(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user_data = UserData.objects.get(username=username)
            except UserData.DoesNotExist:
                messages.error(request, 'Username or password is invalid.')  # Generic error message
                return render(request, 'sidequest/login.html', {'form': form})

            # Check if password matches
            if user_data.password == password:
                return redirect('home')  # Redirect to home page on successful login
            else:
                messages.error(request, 'Username or password is invalid.')  # Generic error message
                return render(request, 'sidequest/login.html', {'form': form})

    else:
        form = UserDataForm()

    return render(request, 'sidequest/login.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            user_data = UserData.objects.get(username=username)
        except UserData.DoesNotExist:
            UserData.objects.create(username=username, password=password)
            return redirect('home')
    else:
        form = UserDataForm()
    return render(request, 'sidequest/login.html', {'form': form})