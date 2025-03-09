from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, time

STATUS_CHOICES = (
    ('Not Started', 'Not Started'),
    ('draft', 'Draft'),
    ('Downloaded', 'Downloaded'),
    ('Updated', 'Updated'),
    ('published', 'Published'),
    ('Error', 'Error'),
)

SPECIFIC_TIMES = [
    time(2, 30),   # 8:00 AM
    time(5, 30),   # 8:00 AM
    time(18, 0),  # 12:00 PM
    time(21, 30),  # 3:00 PM
    time(23, 0),  # 6:00 PM
]


# Create your models here.
class Content(models.Model):
    link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    body = models.TextField()
    hashtags = models.TextField()
    isdub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.link} - {self.upload_time}"
    
    @classmethod
    def get_next_upload_time(cls):
        # Get the last Content object by upload_time
        last_content = cls.objects.order_by('-upload_time').first()

        if last_content:
            last_upload_time = last_content.upload_time
        else:
            # If no Content exists, start from the first time today
            last_upload_time = timezone.make_aware(
                datetime.combine(timezone.now().date(), SPECIFIC_TIMES[0])
            )

        # Find the next available time
        for specific_time in SPECIFIC_TIMES:
            next_upload_time = timezone.make_aware(
                datetime.combine(last_upload_time.date(), specific_time)
            )
            if next_upload_time > last_upload_time:
                return next_upload_time

        # If no time is available today, use the first time tomorrow
        first_time_tomorrow = timezone.make_aware(
            datetime.combine(last_upload_time.date() + timedelta(days=1), SPECIFIC_TIMES[0])
        )
        return first_time_tomorrow

    def save(self, *args, **kwargs):
        # Automatically set upload_time if it's not provided
        if not self.upload_time:
            self.upload_time = self.get_next_upload_time()
        super().save(*args, **kwargs)