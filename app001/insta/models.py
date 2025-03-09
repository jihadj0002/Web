from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class InstagramAccount(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=120)
    access_token = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Instagram Account"
        verbose_name_plural = "Instagram Accounts"
        
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    instagram_account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    
    caption = models.TextField()
    media = models.ImageField(upload_to='posts/')
    
    sheduled_time = models.DateTimeField()
    
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"   
        
class PostAnalytics(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)
    reach = models.IntegerField(default=0)
    saved = models.IntegerField(default=0)
    engagement = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.caption
    
    class Meta:
        verbose_name = "Post Analytics"
        verbose_name_plural = "Post Analytics"