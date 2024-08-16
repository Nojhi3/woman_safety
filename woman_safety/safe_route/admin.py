from django.contrib import admin
from safe_route.models import recordedCrime

# Register your models here.

@admin.register(recordedCrime)
class CrimeModelAdmin(admin.ModelAdmin):
    list_display = ['road_name', 'latitude', 'longitude']