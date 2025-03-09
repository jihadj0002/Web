from django.shortcuts import render, redirect, get_object_or_404
from .models import Content
from django.utils import timezone

from datetime import datetime, timedelta

# Create your views here.
def index(request):
    now  = timezone.now()
    status = request.GET.get('status')
    hashtags = request.GET.get('hashtags')
    isdub = request.GET.get('isdub')
    upload_time_start = request.GET.get('upload_time_start')
    upload_time_end = request.GET.get('upload_time_end')

    one_day_ago = now - timedelta(days=1)
    contents = Content.objects.filter(upload_time__gte=one_day_ago).exclude(status='Completed').order_by('-upload_time')
    
    # Apply filters
    if status:
        contents = contents.filter(status=status)
    if status:
        contents = contents.filter(status="All")
    if hashtags:
        contents = contents.filter(hashtags__icontains=hashtags)
    if isdub:
        contents = contents.filter(isdub=(isdub == "true"))

    # Filter by upload_time range
    if upload_time_start:
        upload_time_start = datetime.strptime(upload_time_start, '%Y-%m-%d')
        contents = contents.filter(upload_time__gte=upload_time_start)
    if upload_time_end:
        upload_time_end = datetime.strptime(upload_time_end, '%Y-%m-%d')
        contents = contents.filter(upload_time__lte=upload_time_end)
    
    context = {
        'contents': contents
    }
    return render(request, "hiking/index.html", context)


def add(request):
    
    if request.method == "POST":
        link = request.POST['link']
        status = request.POST['status']
        body = request.POST['body']
        hashtags = request.POST['hashtags']
        isdub = request.POST.get('isdub', False)
        
        
        content = Content(link=link, status=status, body=body, hashtags=hashtags, isdub=isdub)
        content.save()
        return redirect('hiking:index')
    
    return render(request, "hiking/edit.html")

def delet(request, pk):
    content = Content.objects.get(pk=pk)
    content.delete()
    return redirect('hiking:index')

def edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    
    if request.method == "POST":
        content.link = request.POST['link']
        content.status = request.POST['status']
        content.body = request.POST['body']
        content.hashtags = request.POST['hashtags']
        content.isdub = request.POST.get('isdub', False)
        content.upload_time = request.POST['upload_time']
        content.save()
        return redirect('hiking:index')
    
    
    context = {
        'content': content
    }
    return render(request, "hiking/edit.html", context)