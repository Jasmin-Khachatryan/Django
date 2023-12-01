from django.urls import path
from burgers.views import burger

urlpatterns = [
    path("", burger, name="burgers"),

]
