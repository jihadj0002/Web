# run <python manage.py load_data "D:\\Code\\Python\\New_Learning\\DJango\\Web\\app001\\hiking\\hike.csv"> in the terminal

import csv
from django.core.management.base import BaseCommand
from hiking.models import Content
from datetime import datetime

class Command(BaseCommand):
    help = "Load data from csv file"

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Indicates the file path')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        self.stdout.write(f"Loading data from: {path}")  # Debug print
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) >= 6:
                    Content.objects.get_or_create(
                        link=row[0],
                        status=row[1],
                        body=row[2],
                        hashtags=row[5],
                        isdub=row[4].lower() == 'true',
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                        upload_time=datetime.strptime(row[3], "%m/%d/%Y %H:%M:%S")
                    )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))