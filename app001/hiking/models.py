from django.db import models

STATUS_CHOICES = (
    ('Not Started', 'Not Started'),
    ('draft', 'Draft'),
    ('Downloaded', 'Downloaded'),
    ('Updated', 'Updated'),
    ('published', 'Published'),
    ('Error', 'Error'),
)

# Create your models here.
class Content(models.Model):
    link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    body = models.TextField()
    hashtags = models.TextField()
    isdub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.link