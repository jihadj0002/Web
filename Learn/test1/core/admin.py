from django.contrib import admin
from .models import Vendor, Category, Product, ProductImage, ProductVarient, Cart, CartItem, Coupon, Order, OrderItem
from .models import ShippingAddress, Payment, ProductReview, Wishlist, BlogPost, FAQ, LegalPage, NewsLetterSubscription, ReturnRequest


from django.utils.html import format_html




# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3 #Number of extra forms to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_image', 'title', 'price', 'stock', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active','is_featured', 'created_at')
    search_fields = ('title', 'description', 'sku')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price', 'stock', 'is_active', 'is_featured')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'discount_price',  'stock', 'sku', 'slug', 'category')
        }),
        ('Availability', {
            'fields': ('is_active', 'is_featured')
        }),
    )
    save_on_top = True
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)
    mark_as_active.short_description = "Mark selected products as active"
    
    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)
    mark_as_inactive.short_description = "Mark selected products as inactive"
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_image','name', 'slug', 'created_at', 'is_active', 'is_featured')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    

class VendorAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_phone', 'business_address', 'rating', 'approved')
   
admin.site.register(Vendor, VendorAdmin)


class ProductVarientAdmin(admin.ModelAdmin):
    list_display = ('product', 'value', 'sku', 'quantity', 'price_adjustment')
    
admin.site.register(ProductVarient, ProductVarientAdmin)

    
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid_status', 'created_at')    

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    
admin.site.register(CartItem, CartItemAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'start_date', 'end_date', 'is_active')
    list_filter = ('discount_type', 'is_active')
    search_fields = ('code',)
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'

admin.site.register(Coupon, CouponAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_number', 'total', 'status', 'created_at')

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

admin.site.register(OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order', 'first_name', 'city')

admin.site.register(ShippingAddress, ShippingAddressAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'amount', 'status', 'created_at')

admin.site.register(Payment, PaymentAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
admin.site.register(ProductReview, ProductReviewAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    
admin.site.register(Wishlist, WishlistAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

admin.site.register(BlogPost, BlogPostAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')
admin.site.register(FAQ, FAQAdmin)

class LegalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
admin.site.register(LegalPage, LegalPageAdmin)

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
admin.site.register(NewsLetterSubscription, NewsletterSubscriptionAdmin)

class ReturnRequestAdmin(admin.ModelAdmin):
    list_display = ('order', 'reason', 'status', 'request_date')




    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)