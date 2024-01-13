from django.urls import path
from .views import RestaurantCreateView, RestaurantListView, RestaurantDetailView

urlpatterns = [
    path("", RestaurantListView.as_view(), name="restaurant"),
    path("add-restaurant", RestaurantCreateView.as_view(), name='create_restaurant'),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name="res_detail"),
    ]
