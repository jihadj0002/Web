from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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



@login_required(login_url="/login/")
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return redirect("recipe:index")

@login_required(login_url="/login/")
def update_recipe(request, pk):
    
    recipe = Recipe.objects.get(id=pk)
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        recipe.title = title
        recipe.description = description
        
        recipe.save()
        return redirect('/')
    context = {
        "recipe":recipe,
    }
    return render(request, "recipe/update_recipe.html", context)

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

def signup(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect("recipe:signup")
            user = User.objects.create(username=username) #Here using password=password dosent works because thats not clean data I guess. 
            user.set_password(password)
            
            user.save()
            messages.success(request, "User Created Successfully")
            
        except Exception as e:
            messages.error(request, "Smething Went Wrong")
    
    return render(request, "recipe/sign-up.html")
