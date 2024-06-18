from django.shortcuts import render, redirect
from .forms import UserDataForm

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

def add_user(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            # Redirect to a success page or perform other actions
    else:
        form = UserDataForm()

    return render(request, 'sidequest/login.html', {'form': form})