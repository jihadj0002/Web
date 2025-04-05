from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'f_products': Product.objects.filter(is_featured=True).order_by('-created_at')[:4],
        'products': products,
        'categories': categories[:3],
    }
    return render(request, "core/index.html", context)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, "core/shop.html", context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "core/cateories.html", context)