from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import messages

# Create your views here.

#Login Page For User
def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            print("Username: ", username)
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("core:index")
            else:
                messages.error(request, "Invalid Username or Password")
                print("Invalid Username or Password")
                return render(request, "userauth/login.html")
        except Exception as e: 
            messages.error(request, "Invalid` Username or Password")
            print("Exception: ", e)
            return render(request, "userauth/login.html")
    return render(request, "userauth/login.html")

def register(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate data
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('userauth:register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('userauth:register')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            auth_login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('core:index')  # Replace with your home page URL name
        except Exception as e:
            messages.error(request, f'Error during registration: {str(e)}')
            return redirect('userauth:register')
    
    return render(request, 'userauth/register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("core:index")


def profile(request):
    return render(request, "userauth/profile.html")