from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
import uuid
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(null=True, blank=True, default=uuid.uuid4, editable=False)
    
    
    def __str__(self):
        return self.username
    
    
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    business_name = models.CharField(max_length=200)
    business_address = models.CharField(max_length=300)
    business_phone = models.CharField(max_length=15, null=True, blank=True)
    approved = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.business_name
    

    
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=True )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    is_featured = models.BooleanField(default=False)
    
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    
    
    

class Product(models.Model):
    
    CONDITION_CHOICES = (
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    )
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),   
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    compare_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50, unique=True)
    
    barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lenght = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    tax_class = models.CharField(max_length=50, null=True, blank=True)
    
    seo_title = models.CharField(max_length=200, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    seo_keywords = models.CharField(max_length=200, null=True, blank=True)
    
    
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    stock = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.sku:
            self.sku = f"SKU-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
    
    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            discount = ((self.price - self.discount_price) / self.price) * 100
            return round(discount)
        
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
    def is_in_stock(self):
        return self.stock > 0 and self.staus == 'published'
    
    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=200, null=True, blank=True)
    
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"Image for {self.product.title}"
    
