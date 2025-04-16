from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, ProductImage
import json, requests

from django.http import HttpResponse
from django.core.files import File
from io import BytesIO


# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'f_products': Product.objects.filter(is_featured=True).order_by('-created_at')[:4],
        'products': products,
        'categories': categories[:3],
    }
    return render(request, "core/index.html", context)


def shop(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    paginator = Paginator(products, 6)  # Show 6 products per page
    page_number = request.GET.get('page')
    
    try:
        products = paginator.get_page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, "core/shop.html", context)

def view_product(request, slug):
    product = get_object_or_404(Product.objects.prefetch_related('images'), slug=slug)
    products = Product.objects.all().order_by('-created_at')[:4]
    categories = Category.objects.all()
    context = {
        'product': product,
        'products': products,
        'categories': categories,
    }
    return render(request, "core/detail.html", context)

def categories(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')[:6]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "core/cateories.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")
def cart(request):
    return render(request, 'core/cart.html')