from django.urls import path
from pizza.views import pizza, about_us, add_pizza, update_pizza, delete_pizza

urlpatterns = [
    path("", pizza, name="pizzas"),
    path("about-us/", about_us, name="about_us"),
    path("add-pizza/", add_pizza, name="add_pizza"),
    path("update-pizza/<int:pk>/", update_pizza, name="update_pizza"),
    path("delete-pizza/<int:pk>/", delete_pizza, name="delete_pizza")
]
