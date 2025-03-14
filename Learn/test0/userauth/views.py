from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages



#Login Page For User
def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("base:index")
            else:
                messages.error(request, "Invalid Username or Password")
                print("Invalid Username or Password")
                return render(request, "userauth/login.html")
        except Exception as e: 
            messages.error(request, "Invalid Username or Password")
            print("Exception: ", e)
            return render(request, "userauth/login.html")
    return render(request, "userauth/login.html")


def logoutt(request):
    logout(request)
    return redirect("userauth:login")

def signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect("userauth:signup")
            user = User.objects.create(username=username) #Here using password=password dosent works because thats not clean data I guess. 
            user.set_password(password)
            
            user.save()
            messages.success(request, "User Created Successfully")
            
        except Exception as e:
            messages.error(request, "Smething Went Wrong")
    
    return render(request, "userauth/sign-up.html")
