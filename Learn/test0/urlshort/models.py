from django.db import models

# Create your models here.
class UrlData(models.Model):
    url = models.URLField(max_length=200)
    #shortcode = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.url} - {self.slug}"
    
    def __unicode__(self):
        return f"{self.url} - {self.slug}"
    
    def get_short_url(self):
        pass
        #return "http:// 