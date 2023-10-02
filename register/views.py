from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method =="GET":
        form = RegisterForm()
        return render(request, 'register/register.html', { 'form' : form })
    if request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register/register.html', {'form': form})