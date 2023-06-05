from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already registered and logged in.")
        return redirect("home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("home")  # Replace 'home' with your desired URL
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("login")
