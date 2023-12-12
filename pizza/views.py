from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from pizza.models import Pizza


def pizza(request):
    pizzas = Pizza.objects.all()
    paginator = Paginator(pizzas, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "pizza/all_pizza.html", {"pizzas": page_obj})


def about_us(request):
    return render(request, "pizza/about_us.html")


def pizza_info(request, pk):
    reference_pizza = get_object_or_404(Pizza, pk=pk)

    price_range = 30
    calories_range = 40

    similar_pizzas = Pizza.objects.filter(
        Q(price__range=(reference_pizza.price - price_range, reference_pizza.price + price_range)) |
        Q(calories__range=(reference_pizza.calories - calories_range, reference_pizza.calories + calories_range))
    ).exclude(id=pk)

    context = {
        'pizzas': reference_pizza,
        'all_pizza': similar_pizzas,
    }

    return render(request, 'pizza/pizza_info.html', context)