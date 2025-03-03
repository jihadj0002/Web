from django.db import models

LANUAGE_CHOICES = (
    ("EN", "English"),
    ("BN", "Bengali"),
    ("HN", "Hindi"),
)

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    
    lyrics = models.TextField(verbose_name="Lyrics")
    language = models.CharField(max_length=2, choices=LANUAGE_CHOICES, default="BN")
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.language}"
    
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
    
    