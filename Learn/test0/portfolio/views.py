from django.shortcuts import render, redirect
from .models import Photos, Messages

# Create your views here.
def index(request):
    
    if request.method == 'GET':
        fullname = request.GET.get('fullname')
        email = request.GET.get('email')
        message = request.GET.get('message')
        if fullname and email and message:
            # Save the message to the database or send an email
            Messages.objects.create(name=fullname, email=email, message=message)
            # Optionally, you can redirect to a success page or show a success message
            return redirect('portfolio:index')
        
    
    return render(request, "portfolio/sus.html")

def about(request):
    return render(request, "portfolio/about.html")

def porfolio(request):
    return render(request, "portfolio/portfolio.html")

def services(request):
    return render(request, "portfolio/services.html")

def resume(request):
    return render(request, "portfolio/resume.html")

def contact(request):
    return render(request, "portfolio/contact.html")