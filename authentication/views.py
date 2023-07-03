from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password!'
            return render(request, 'auth/login.html', {'error': error})
    
    return render(request, 'auth/login.html')



def signup(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                        first_name=first_name, 
                        last_name=last_name,
                        email=email,
                        username=username, password=password)
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                error = 'Username already exists!'
        else:
            error = 'Passwords do not match!'
        
        return render(request, 'auth/signup.html', {'error': error})
    
    return render(request, 'auth/signup.html')



def forgot_password(request):
    return render(request, 'auth/forgot_password.html')