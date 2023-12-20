from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from restaurant.models import Restaurant
from .forms import RestaurantForm, RestaurantPizzaFormSet, RestaurantBurgerFormSet
from pizza.models import Pizza
from burgers.models import Burger


def restaurant(request):
    restaurants = Restaurant.objects.all().prefetch_related("pizza", "burger").order_by("pk")
    paginator = Paginator(restaurants, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "restaurant/restaurant.html", {"restaurants": page_obj})


def detail_page(request, pk):
    res_detail = get_object_or_404(Restaurant, pk=pk)
    return render(request, "restaurant/detail.html", {"restaurant": res_detail})


def burger_detail_page(request, pk):
    burger_detail = get_object_or_404(Restaurant, pk=pk)
    return render(request, "restaurant/burger_detail.html", {"restaurant":burger_detail})


def create_restaurant(request):
    if request.method == "POST":
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
    else:
        form = RestaurantForm()
        formset_pizza = RestaurantPizzaFormSet(prefix="pizza_formset", queryset=Pizza.objects.none())
        formset_burger = RestaurantBurgerFormSet(prefix="burger_formset", queryset=Burger.objects.none())

    return render(request, "restaurant/add_res.html", {"form": form, "formset_pizza": formset_pizza,
                                                       "formset_burger": formset_burger})


