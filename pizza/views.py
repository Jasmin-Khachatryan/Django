from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

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
    pizzas = get_object_or_404(Pizza, pk=pk)
    return render(request, "pizza/pizza_info.html", {"pizzas": pizzas})


