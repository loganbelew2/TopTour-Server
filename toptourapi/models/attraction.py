from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    rating = models.FloatField()
    total_ratings = models.IntegerField()
    photo_url = models.CharField(max_length=255)
    price_level = models.IntegerField()

    def __str__(self):
        return self.name
