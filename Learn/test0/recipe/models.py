from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200, default="Chicken Curry")
    description = models.TextField(default="This is a chicken curry recipe.")
    
    
    day = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipess"