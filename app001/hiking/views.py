from django.shortcuts import render
from .models import Content

# Create your views here.
def index(request):
    contents = Content.objects.all()
    
    context = {
        'contents': contents
    }
    return render(request, "hiking/index.html", context)