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
    

class ProductVarient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=5)
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f"SKU-(uuid.uuid4().hex[:8])"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.product.name} - {self.name}: {self.value}"
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
    session_key = models.CharField(max_length=40, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        return f"Cart {self.session_key}"
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())
    
    def get_subtotal(self):
        return sum(item.get_total_price() for item in self.items.all())
    
    def get_total(self):
        subtotal = self.get_subtotal()
        # Add shipping and taxes if applicable
        return subtotal
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    varient = models.ForeignKey(ProductVarient, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_total_price(self):
        if self.varient:
            return (self.product.price + self.varient.price_adjustment) * self.quantity
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.title} - {self.quantity} pcs"
    
    

    
    
class Coupon(models.Model):
    DISCOUNT_TYPES = (
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    )
    
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, default='percentage')
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(null=True, blank=True)
    used_count = models.PositiveIntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Coupon {self.code} - {self.discount_value} {self.discount_type} -- {self.start_date} to {self.end_date}"
    
    def is_valid(self, user=None, cart_total=None):
        if not self.is_active:
            return False
        if self.start_date and timezone.now() < self.start_date:
            return False
        if self.end_date and timezone.now() > self.end_date:
            return False
        if cart_total and self.min_order_value and cart_total < self.min_order_value:
            return False
        if self.usage_limit and self.used_count >= self.usage_limit:
            return False
        return True
    
    
    
class Order(models.Model):
    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
        ('refunded', 'Refunded'),
    )
    
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ('cancelled', 'Cancelled'),
    )
    
    order_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    stauts = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    coupon_code = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"ORD-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Order {self.order_number} - {self.user.username if self.user else 'Guest'}"
    
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'order_number': self.order_number})
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', null=True, blank=True)
    varient = models.ForeignKey(ProductVarient, on_delete=models.SET_NULL, null=True, blank=True)
    quitity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def get_total_price(self):
        if self.varient:
            return (self.price + self.varient.price_adjustment) * self.quantity
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.product.title} - {self.quantity} pcs -- (Order # {self.order.order_number})"
    
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    special_instructions = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Shipping Address for Order {self.order.order_number}"
    
    

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash_on_delivery', 'Cash on Delivery'),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Order.PAYMENT_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(auto_now_add=True)
    raw_response = models.JSONField(null=True, blank=True)
    is_refunded = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Payment for Order {self.order.order_number} - {self.payment_method}"
    
class ProductReview(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=200)
    review = models.TextField()
    
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'user')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Review for {self.product.title} by {self.user.username if self.user else 'Guest'}"
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, related_name='wishlists')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Wishlist"