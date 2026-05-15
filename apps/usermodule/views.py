from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'usermodule/register.html', {'form': form})



def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, 'Login successfully')

            return redirect('/')

        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'usermodule/login.html')


def logout_user(request):

    logout(request)

    return redirect('login')