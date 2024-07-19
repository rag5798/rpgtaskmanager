from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserDataForm, TaskForm, TaskCreationForm, CharacterCreationForm
from .models import UserData, Task, User, Character
from django.utils.timezone import now
import random

def home(request):
    return render(
        request,
        "sidequest/index.html"
    )

@login_required
def task(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    character = Character.objects.filter(user_id=user_id)
    return render(
        request,
        "sidequest/task.html",
        {
            "tasks": tasks,
            "stats": character
        } 
        # Pass the tasks to the template context
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
            # Save the user
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()

            # Create and save the character for the new user
            character_form = CharacterCreationForm({'character_name': user.username})
            character = character_form.save(user=user, commit=True)  # Save the character

            # Redirect to the character roll page with the character context
            return render(request, 'sidequest/character_roll.html', {'character': character})
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
        form = TaskCreationForm(request.POST)
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

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id, user_id=request.user.id)
    character = get_object_or_404(Character, user_id=request.user.id)
    if request.method == 'POST':
        task.completed = True
        task.updated_at = now()
        character.attacks += 1
        task.save()
        character.save()  # Save the character after incrementing attacks
        return redirect('task')  # Redirect back to the task list page
    
@login_required
def character_selection(request):
    if request.method == 'POST':
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            character = form.save(request.user)
            return redirect('character_roll', character_stats_id=character.id)
    else:
        form = CharacterCreationForm()
    return render(request, 'sidequest/character_selection.html', {'form': form})

@login_required
def character_roll(request, character_id):
    # Retrieve the character based on the ID
    character = get_object_or_404(Character, id=character_id)

    # Pass character attributes to the template
    context = {
        'character': character
    }

    return render(request, 'sidequest/character_roll.html', context)