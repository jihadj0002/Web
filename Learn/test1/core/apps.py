from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    label = 'my_core'  # Add a custom label if needed
    
    def ready(self):
        # Import and register your User model
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.unregister(User)  # Unregister if already registered
        admin.site.register(User, UserAdmin)  # Register with UserAdmin