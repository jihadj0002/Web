from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group

import uuid

# Create your models here.

class User(AbstractUser):
    # Custom fields
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)

    # Fix for groups conflict
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="core_user_set",  # Changed
        related_query_name="core_user",
    )
    
    def __str__(self):
        return self.username
    