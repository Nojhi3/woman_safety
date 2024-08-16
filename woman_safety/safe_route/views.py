from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages
from django.conf import settings
import csv
from safe_route.mixins import Directions

def home(request):
    return render(request, 'safe_route/home.html')

def get_crimedata(request):
    if request.method == 'POST':
        try:
            call_command('importcsv')
            messages.success(request, 'Successfully imported Data.')
        except Exception as e:
            messages.error(request, f'Error importing data: {e}')
        return redirect('/')
    else:
        return redirect('/')


def display_csv(request):
    csv_file_path = settings.BASE_DIR / 'data' / 's2.csv'

    data = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return render(request, 'safe_route/display.html', {'data': data})

def diplay_map(request):

    csv_file_path = settings.BASE_DIR / 'data' / 's2.csv'

    data = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return render(request, 'safe_route/map.html', {'data': data})
