from django.db import models

RATE_CHOICES = [(0, "---")] + [(rate, f"{rate}") for rate in range(1, 11)]
PRODUCT_TYPE_CHOICES = [("pizza", "pizza"), ("burger", "burger")]

class UserTypeChoice(models.TextChoices):
    client = "client", "Client"
    business = "business", "Business"
