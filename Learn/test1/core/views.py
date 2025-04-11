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

def readfile(request):
    i = 1
    url = "https://dummyjson.com/products/" + str(i)
    try:
    # Fetch data
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # print(json.dumps(data, indent=4))  # Debugging
        print(data['title'])
        # Calculate discount
        discount_amount = (data['discountPercentage'] * data['price']) / 100

        # Get or create category
        category, _ = Category.objects.get_or_create(name=data['category'])

        image_url = data.get('image') 
        # Create product
        if image_url:
            print(f"Image URL: {image_url}")
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                # Create a Django-friendly File object
                image_file = BytesIO(image_response.content)
                image_name = image_url.split('/')[-1]  # Extract filename from URL

                # Create the product and assign the image
                product = Product.objects.create(
                    title=data['title'],
                    description=data['description'],
                    price=data['price'],
                    category=category,
                    discount_price=discount_amount,
                    stock=data['stock'],
                    image = File(image_file, name=image_name),  # Save the image
                    # sku=data['sku'],  # Handle SKU uniqueness as discussed earlier
                )
                print(f"Product created: {product.title}")

            # Save images (if ProductImage model exists)
            # for img_url in data['images']:
            #     ProductImage.objects.create(product=product, image_url=img_url)

            return HttpResponse(f"Successfully imported product: {data['title']}")

    except requests.RequestException as e:
        return HttpResponse(f"API Error: {e}", status=500)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)
    
# return render(request, "core/import.html", {'content': content})