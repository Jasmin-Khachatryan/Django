from django.urls import path
from burgers.views import burger, add_burger, update_burger, delete_burger

urlpatterns = [
    path("", burger, name="burgers"),
    path("add-burger/", add_burger, name="add_burger"),
    path("update-burger/<int:pk>/,", update_burger, name="update_burger"),
    path("delete-burger/<int:pk>/", delete_burger, name="delete_burger")

]