from django.shortcuts import render
from .models import Song

# Create your views here.
def index(request):
    songs = Song.objects.all()
    
    context = {
        "songs":songs,
    }
    return render(request, "song/index.html", context)


def detail(request, id):
    song = Song.objects.get(id=id)
    
    context = {
        "song":song,
    }
    return render(request, "song/detail.html", context)