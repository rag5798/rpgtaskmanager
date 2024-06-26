from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserDataForm, TaskForm, TaskCreationForm
from .models import UserData, Task, User

def home(request):
    return render(
        request,
        "sidequest/index.html"
    )

@login_required
def task(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    return render(
        request,
        "sidequest/task.html",
        {"tasks": tasks}  # Pass the tasks to the template context
    )

def character(request):
    return render(
        request,
        "sidequest/character.html",
    )

def user_login(request):
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

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                return redirect('home')  # Redirect to a home page or any other page
    else:
        form = AuthenticationForm()
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'sidequest/add_user.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'protected_page.html')

# views.py
@login_required
def task_creation(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user
            task.completed = False
            task.task_completion_counter = 0
            task.repetitive = form.cleaned_data['repetitive']
            task.save()
            return redirect('task')
    else:
        form = TaskCreationForm()
    return render(request, 'sidequest/task_creation.html', {'form': form})



