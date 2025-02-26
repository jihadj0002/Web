from django.shortcuts import render, redirect
#from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("core:index")
    
    
    # if request.method == "POST":
    #     username = request.POST.get("email")
    #     password = request.POST.get("password")
    #     user = authenticate(request, email=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, "You Are Logged In")
    #         return redirect("core:index")
    #     else:
    #         messages.warning(request, "User Does Not Exist Create An Account")
        
    return render(request, "userauth/login.html")    



# def register_view(request):
    
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")
#             messages.success(request, f"Hey {username}, Your Account was Created SuccessFully..")
#             new_user = authenticate(username=username, password=password)
#             login(request, new_user)
#             return redirect("core:index")
    
#     form = UserRegistrationForm()
    
#     context = {
#         "form":form
#     }
    
#     return render(request, "userauth/sign-up.html", context)

# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logout Success")
#     return redirect("core:index")