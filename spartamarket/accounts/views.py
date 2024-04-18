from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

def login(request):
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect("accounts:test")
    context = { "form" : form}
    return render(request, "accounts/login.html", context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("accounts:test")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ("accounts:test")
    else:
        form = CustomUserCreationForm()
    context = { "form" : form }
    return render(request, "accounts/signup.html", context)

def test(request):
    return render(request, "accounts/test.html")