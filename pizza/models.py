from django.db import models
from restaurant.models import Restaurant
from django.urls import reverse
from helpers.media_upload import upload_pizza_image


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField(default=0)
    prepare_time = models.FloatField(null=True, blank=True)
    calories = models.FloatField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_pizza_image, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name="pizza", null=True)

    def get_absolute_url(self):
        return reverse("pizza_info", kwargs={"pk": self.pk})

    def __str__(self):
        return self.pizza_name
