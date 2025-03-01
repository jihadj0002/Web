from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    
    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, "ecom/index.html", context)

def product_list(request):
    
    products = Product.objects.all()
    categorys = Category.objects.all()
    
    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, "ecom/product_list.html", context)

def category_list(request):
    
    categorys = Category.objects.all()
    
    context = {
        "categorys": categorys,
    }
    return render(request, "ecom/category_list.html", context)

def product_detail(request, slug):
    
    product = Product.objects.get(slug=slug)
    
    context = {
        "product": product,
    }
    return render(request, "ecom/product_detail.html", context)