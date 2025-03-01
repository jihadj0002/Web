from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
class Product(models.Model):
    
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    other_image = models.FileField(upload_to='products/', null=True, blank=True)
    
    categories = models.ManyToManyField(Category, blank=True)
    stock = models.IntegerField(default=20)

    active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
