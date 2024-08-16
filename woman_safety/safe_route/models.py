from django.db import models

class recordedCrime(models.Model):
    road_name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.road_name