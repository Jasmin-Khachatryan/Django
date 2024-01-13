from django.urls import path
from pizza.views import AboutUsView, PizzaListView, PizzaCreateView, UpdatePizzaView, DeletePizzaView, PizzaDetailView

urlpatterns = [
    path("", PizzaListView.as_view(), name="pizzas"),
    path("about-us/", AboutUsView.as_view(), name="about_us"),
    path("add-pizza/", PizzaCreateView.as_view(), name="add_pizza"),
    path("update-pizza/<int:pk>/", UpdatePizzaView.as_view(), name="update_pizza"),
    path("delete-pizza/<int:pk>/", DeletePizzaView.as_view(), name="delete_pizza"),
    path("<int:pk>/pizza/info/", PizzaDetailView.as_view(), name="pizza_info"),
]
