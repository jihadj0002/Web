from django.shortcuts import render, redirect
from .forms import ShortenURLForm
from .models import UrlData
import random, string
# Create your views here.

def index(request):
    
    data = UrlData.objects.all()
    
    if request.method == "POST":
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            
            slug = ''.join(random.choice(string.ascii_letters) for x in range(6))
            url = form.cleaned_data["url"]
            
            new_url = UrlData.objects.create(url=url, slug=slug)
            new_url.save()
            print("Saved")
            return redirect("urlshort:view_url", slug=slug)
        
    else:
        form = ShortenURLForm()
    
    context = {
        "urls":data,
    }
        
    return render(request, "urlshort/index.html")

def view_url(request, slug):
    
    data = UrlData.objects.get(slug=slug)
    
    context = {
        'url':data,
    }
    
    return render(request, "urlshort/view_url.html", context)
    