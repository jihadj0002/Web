from django.test import TestCase
import csv
from django.core.management.base import BaseCommand
from hiking.models import Content
from datetime import datetime

# Create your tests here.

now = datetime.now()


class Command(BaseCommand):
    help = "Load data from csv file"
    
    path = "D:\Code\Python\New_Learning\DJango\Web\app001\hiking\hike.csv"
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Indicates the file path')
        
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                
                #Links,Status,Data,Due date,Content Done?,HashTags,Stage,Notes
                # link = models.URLField()
                # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
                # body = models.TextField()
                # hashtags = models.TextField()
                # isdub = models.BooleanField(default=False)
                # created_at = models.DateTimeField(auto_now_add=True)
                # updated_at = models.DateTimeField(auto_now=True)
                # upload_time = models.DateTimeField(auto_now=True)
                    Content.objects.get_or_create(
                    link=row[0],
                    status=row[1],
                    body=row[2],
                    hashtags=row[5],
                    isdub=row["False"],
                    created_at=row[now],
                    updated_at=row[now],
                    upload_time=row[3]
                )
            
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
    