from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active','is_featured', 'created_at')
    search_fields = ('title', 'description', 'sku')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price', 'stock', 'is_active', 'is_featured')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'discount_price', 'image', 'stock', 'sku', 'slug', 'category')
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
    list_display = ('name', 'slug', 'created_at', 'is_active', 'is_featured')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)