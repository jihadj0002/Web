from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GRADE_CHOICES = (
    ("A+", "A+"),
    ("A", "A"),
    ("B+", "B+"),
    ("B", "B"),
    ("C+", "C+"),
    ("C", "C"),
    ("D+", "D+"),
    ("D", "D"),
    ("F", "F"),
)
UNIVERSITY_CHOICES = (
    ("DIU", "DIU"),
    ("NSU", "NSU"),
    ("BRAC", "BRAC"),
    ("AIUB", "AIUB"),
    ("EWU", "EWU"),
    ("IUB", "IUB"),
    ("UIU", "UIU"),
)

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    credit = models.IntegerField(default=3)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="A+")
    

    def __str__(self):
        return f"{self.name} - {self.grade}, Credit {self.credit}"
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "Subject"