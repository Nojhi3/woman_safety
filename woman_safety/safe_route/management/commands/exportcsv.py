import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from safe_route.models import recordedCrime
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Load data from sample file'

    def handle(self, *args, **kwargs):
        data_dir = os.path.join(settings.BASE_DIR, 'data')

        csv_file_path = os.path.join(data_dir, 'sample.csv')
        try:
            df = pd.read_csv(csv_file_path)
            df['road_name'] = df['road_name'].fillna(value='unknown')
            df['latitude'] = df['latitude'].fillna(value='unknown')
            df['longitude'] = df['longitude'].fillna(value='unknown')

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("not found csv file"))
            return 
        
        records = []

        for _, row in df.iterrows():
            road_name = row['road_name']
            latitude = row['latitude']
            longitude = row['longitude']
            records.append([road_name,latitude,longitude])

        self.stdout.write(self.style.SUCCESS(
            'Successfully retrived All data'
        ))