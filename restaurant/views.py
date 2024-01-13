from django.shortcuts import render, get_object_or_404, redirect
from restaurant.models import Restaurant
from .forms import RestaurantForm, RestaurantPizzaFormSet, RestaurantBurgerFormSet
from django.views.generic import ListView, CreateView, View
from pizza.models import Pizza
from burgers.models import Burger


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "restaurant/restaurant.html"
    context_object_name = "restaurants"
    paginate_by = 4

    def get_queryset(self):
        return Restaurant.objects.all().prefetch_related("pizza", "burger").order_by("pk")


class RestaurantDetailView(View):
    template_name = "restaurant/restaurant_detail.html"

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        items = restaurant.pizza.all()

        if burgers := request.GET.get("burgers"):
            if burgers == "True":
                items = restaurant.burger.all()

        context = {
            "restaurant": restaurant,
            "items": items,
        }

        return render(request, self.template_name, context)


class RestaurantCreateView(CreateView):
    template_name = "restaurant/add_res.html"

    def get(self, request):
        form = RestaurantForm()
        formset_pizza = RestaurantPizzaFormSet(prefix="pizza_formset", queryset=Pizza.objects.none())
        formset_burger = RestaurantBurgerFormSet(prefix="burger_formset", queryset=Burger.objects.none())

        return render(request, self.template_name,
                      {"form": form, "formset_pizza": formset_pizza, "formset_burger": formset_burger})

    def post(self, request):
        form = RestaurantForm(request.POST, request.FILES)
        formset_pizza = RestaurantPizzaFormSet(request.POST, request.FILES, prefix="pizza_formset")
        formset_burger = RestaurantBurgerFormSet(request.POST, request.FILES, prefix="burger_formset")

        if form.is_valid() and formset_pizza.is_valid() and formset_burger.is_valid():
            restaurant = form.save()
            pizzas = formset_pizza.save(commit=False)
            burgers = formset_burger.save(commit=False)

            for pizza in pizzas:
                pizza.restaurant = restaurant
                pizza.save()

            for burger in burgers:
                burger.restaurant = restaurant
                burger.save()

            return redirect("restaurant")

        return render(request, self.template_name,
                      {"form": form, "formset_pizza": formset_pizza, "formset_burger": formset_burger})


