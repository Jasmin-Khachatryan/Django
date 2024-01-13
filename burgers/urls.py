from django.urls import path
from burgers.views import BurgerListView, CreateBurgerView, UpdateBurgerView, DeleteBurgerView, BurgerDetailView

urlpatterns = [
    path("", BurgerListView.as_view(), name="burgers"),
    path("add-burger/", CreateBurgerView.as_view(), name="add_burger"),
    path("update-burger/<int:pk>/,", UpdateBurgerView.as_view(), name="update_burger"),
    path("delete-burger/<int:pk>/", DeleteBurgerView.as_view(), name="delete_burger"),
    path("<int:pk>/burger/info/", BurgerDetailView.as_view(), name="burger_info"),


]