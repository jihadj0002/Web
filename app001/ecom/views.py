from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def index(request):
    
    return render(request, "ecom/index.html")

def product_list(request):
    
    products = Product.objects.all()
    categorys = Category.objects.all()
    
    context = {
        "products": products,
        "categorys": categorys,
    }
    return render(request, "ecom/product_list.html", context)