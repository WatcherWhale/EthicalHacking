from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm, AuthForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form':RegisterForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'register.html', {'form':RegisterForm, 'error':'Username already in use.'})
        else:
            return render(request, 'register.html', {'form':AuthForm, 'error':' Passwords do not match.'})

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form':AuthForm})
    else:
        user = authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'form': AuthForm,'error': 'Incorrect username or password.'})
        else:
            login(request,user)
            return redirect('home')
