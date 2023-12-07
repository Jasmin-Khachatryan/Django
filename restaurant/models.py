from django.db import models
from helpers.media_upload import upload_restaurant_image


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_restaurant_image, blank=True)

    def __str__(self):
        return self.restaurant_name
