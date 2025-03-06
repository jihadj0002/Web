from django.shortcuts import render

# Create your views here.
def index(index):
    return render(index, "cgpa/index.html")