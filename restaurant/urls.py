from django.urls import path
from .views import restaurant, detail_page, burger_detail_page, create_restaurant
from pizza.views import pizza_info
from burgers.views import burger_info

urlpatterns = [
    path("", restaurant, name="restaurant"),
    path("<int:pk>/pizzas/", detail_page, name="res_detail"),
    path("<int:pk>/burgers/", burger_detail_page, name="burger_detail"),
    path("<int:pk>/burger/info/", burger_info, name="burger_info"),
    path("<int:pk>/pizza/info/", pizza_info, name="pizza_info"),
    path("add-restaurant", create_restaurant, name='create_restaurant'),

    ]
