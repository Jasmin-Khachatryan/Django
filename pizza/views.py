from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from pizza.models import Pizza
from pizza.forms import PizzaForm


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


def add_pizza(request):
    form = PizzaForm()

    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect("pizzas")

    return render(request, "pizza/add_pizza.html", {"form": form})


def update_pizza(request, pk: int):
    pizza = get_object_or_404(Pizza, pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            pizza_upd = form.save()
            messages.info(request, "Pizza was updated successfully!")

            return redirect(pizza_upd)
    return render(request, "pizza/update_pizza.html", {"form": form})

def delete_pizza(request, pk: int):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == "POST":
        pizza.delete()
        messages.error(request, "pizza was deleted successfully!")
        return redirect("pizzas")
    return render(request, "pizza/delete_pizza.html")





