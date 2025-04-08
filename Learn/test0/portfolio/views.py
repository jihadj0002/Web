from django.shortcuts import render
from .models import Photos

# Create your views here.
def index(request):
    photo = Photos.objects.get(pk=1)
    context = {
        'photo': photo,
    }
    return render(request, "portfolio/index.html")

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