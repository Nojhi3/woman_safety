
from django.urls import path
from safe_route import views

urlpatterns = [
    path('',views.home, name='home'),
    path('safe_route/',views.get_crimedata, name='get_crimedata'),
    path('display/', views.display_csv, name='display_csv'),
    path('map/', views.diplay_map, name='display_map')
]
