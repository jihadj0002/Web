from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages

# Create your views here.
def index(request):
    
    recipes = Recipe.objects.all()
    
    context = {
        "recipes":recipes,
    }
    return render(request, "recipe/index.html", context)

def detail(request, pk):
    
    recipe = Recipe.objects.get(id=pk)
    
    context = {
        "recipe":recipe,
    }
    return render(request, "recipe/detail.html", context)

#Login Page For User
def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("recipe:index")
            else:
                messages.error(request, "Invalid Username or Password")
                print("Invalid Username or Password")
                return render(request, "recipe/login.html")
        except Exception as e: 
            messages.error(request, "Invalid Username or Password")
            print("Exception: ", e)
            return render(request, "recipe/login.html")
    return render(request, "recipe/login.html")


def logoutt(request):
    logout(request)
    return redirect("recipe:login")